from core.api import VirtualizationView, EnvironmentSettingsView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('virtualization', VirtualizationView)
router.register('Environment', EnvironmentSettingsView)
