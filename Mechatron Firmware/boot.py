import storage
import usb_cdc
import supervisor

storage.remount("/", readonly=False)
usb_cdc.enable(console=True, data=True)
supervisor.runtime.autoreload = True
