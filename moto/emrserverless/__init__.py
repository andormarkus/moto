"""emrserverless module initialization; sets value for base decorator."""
from .models import emrserverless_backends
from ..core.models import base_decorator

REGION = "us-east-1"
RELEASE_LABEL = "emr-6.5.0-preview"
mock_emrserverless = base_decorator(emrserverless_backends)
