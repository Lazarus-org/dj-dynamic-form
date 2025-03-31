import sys
from unittest.mock import Mock, patch

import pytest
from rest_framework.permissions import IsAdminUser
from rest_framework.serializers import Serializer
from rest_framework.throttling import UserRateThrottle

from dynamic_form.api.views.base import BaseViewSet
from dynamic_form.tests.constants import PYTHON_VERSION, PYTHON_VERSION_REASON

pytestmark = [
    pytest.mark.api,
    pytest.mark.api_views,
    pytest.mark.skipif(sys.version_info < PYTHON_VERSION, reason=PYTHON_VERSION_REASON),
]


class TestBaseViewSet:
    """
    Tests for the BaseViewSet class.

    This test class verifies the behavior of the `get_queryset` and `get_serializer_class`
    methods in the BaseViewSet, ensuring they function correctly and raise appropriate
    errors when required attributes are not defined.
    """

    @pytest.fixture
    def base_viewset(self):
        """
        Fixture to create an instance of BaseViewSet for testing.
        """
        return BaseViewSet()

    def test_get_queryset_raises_assertion_error_when_not_defined(self, base_viewset):
        """
        Test that `get_queryset` raises an AssertionError when `queryset` is not defined.

        Args:
        ----
            base_viewset (BaseViewSet): An instance of BaseViewSet.

        Asserts:
        --------
            An AssertionError is raised with the message "queryset must be defined in the subclass".
        """
        with pytest.raises(AssertionError) as exc_info:
            base_viewset.get_queryset()
        assert str(exc_info.value) == "queryset must be defined in the subclass"

    def test_get_queryset_returns_queryset_when_defined(self, base_viewset):
        """
        Test that `get_queryset` returns the correct queryset when `queryset` is defined.

        Args:
        ----
            base_viewset (BaseViewSet): An instance of BaseViewSet.

        Asserts:
        --------
            The returned queryset matches the defined `queryset`.
        """
        expected_queryset = Mock()
        base_viewset.queryset = expected_queryset

        queryset = base_viewset.get_queryset()
        assert (
            queryset == expected_queryset
        ), "Expected queryset to match the defined queryset."

    def test_get_serializer_class_raises_assertion_error_when_not_defined(
        self, base_viewset
    ):
        """
        Test that `get_serializer_class` raises an AssertionError when `serializer_class` is not defined.

        Args:
        ----
            base_viewset (BaseViewSet): An instance of BaseViewSet.

        Asserts:
        --------
            An AssertionError is raised with the message "serializer_class must be defined in the subclass".
        """
        with pytest.raises(AssertionError) as exc_info:
            base_viewset.get_serializer_class()
        assert str(exc_info.value) == "serializer_class must be defined in the subclass"

    def test_get_serializer_class_returns_serializer_class_when_defined(
        self, base_viewset
    ):
        """
        Test that `get_serializer_class` returns the correct serializer class when `serializer_class` is defined.

        Args:
        ----
            base_viewset (BaseViewSet): An instance of BaseViewSet.

        Asserts:
        --------
            The returned serializer class matches the defined `serializer_class`.
        """

        class TestSerializer(Serializer):
            pass

        base_viewset.serializer_class = TestSerializer

        serializer_class = base_viewset.get_serializer_class()
        assert (
            serializer_class == TestSerializer
        ), "Expected serializer_class to match the defined serializer_class."

    @patch("dynamic_form.mixins.api.config_api_attrs.config")
    def test_configure_attrs_with_specific_settings(self, mock_config, base_viewset):
        """
        Test that `configure_attrs` uses viewset-specific settings when provided.

        Args:
            mock_config: Mocked config object to simulate settings.
            base_viewset (BaseViewSet): An instance of BaseViewSet with a config_prefix.

        Asserts:
            Attributes are set based on viewset-specific config values.
        """
        base_viewset.config_prefix = "testview"
        mock_config.api_testview_ordering_fields = ["id", "name"]
        mock_config.api_testview_search_fields = ["description"]
        mock_config.api_testview_throttle_classes = [UserRateThrottle]
        mock_config.api_testview_extra_permission_class = IsAdminUser

        base_viewset.configure_attrs()

        assert base_viewset.ordering_fields == ["id", "name"]
        assert base_viewset.search_fields == ["description"]
        assert base_viewset.throttle_classes == [UserRateThrottle]
        assert IsAdminUser in base_viewset.permission_classes

    def test_normalize_throttle_classes_none(self, base_viewset):
        """
        Test that `_normalize_throttle_classes` returns an empty list when input is None.

        Args:
            base_viewset (BaseViewSet): An instance of BaseViewSet.

        Asserts:
            An empty list is returned for None input.
        """
        result = base_viewset._normalize_throttle_classes(None)
        assert result == []

    def test_normalize_throttle_classes_single_class(self, base_viewset):
        """
        Test that `_normalize_throttle_classes` wraps a single throttle class in a list.

        Args:
            base_viewset (BaseViewSet): An instance of BaseViewSet.

        Asserts:
            A single throttle class is returned as a list.
        """
        result = base_viewset._normalize_throttle_classes(UserRateThrottle)
        assert result == [UserRateThrottle]

    def test_normalize_throttle_classes_list(self, base_viewset):
        """
        Test that `_normalize_throttle_classes` processes a list of throttle classes.

        Args:
            base_viewset (BaseViewSet): An instance of BaseViewSet.

        Asserts:
            The list of throttle classes is returned with only valid BaseThrottle subclasses.
        """

        class NotAThrottle:
            pass

        throttle_list = [UserRateThrottle, NotAThrottle]
        result = base_viewset._normalize_throttle_classes(throttle_list)
        assert result == [UserRateThrottle]

    def test_normalize_throttle_classes_invalid_input(self, base_viewset):
        """
        Test that `_normalize_throttle_classes` raises ValueError for invalid input.

        Args:
            base_viewset (BaseViewSet): An instance of BaseViewSet.

        Asserts:
            A ValueError is raised for non-throttle class input.
        """

        class NotAThrottle:
            pass

        with pytest.raises(ValueError) as exc_info:
            base_viewset._normalize_throttle_classes(NotAThrottle)
        assert "Invalid throttle setting" in str(exc_info.value)
