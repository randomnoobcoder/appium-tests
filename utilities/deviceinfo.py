import subprocess


class DeviceProperties:
    @staticmethod
    def deviceName():
        cmd = "adb shell getprop ro.product.model"
        product_model = subprocess.check_output(cmd, shell=True).decode('utf-8').strip()
        return product_model

    @staticmethod
    def platformVersion():
        for device in DeviceProperties.deviceSerial():
            cmd = 'adb -s {} shell getprop ro.build.version.release'.format(device)
            platform_version = subprocess.check_output(cmd, shell=True).decode('utf-8').strip()
            return platform_version

    @staticmethod
    def deviceSerial():
        return set([device.split('\t')[0] for device in
                    (subprocess.check_output('adb devices', shell=True).decode('utf-8')).splitlines() if
                    device.endswith('\tdevice')])

# dp = DeviceProperties
# print(dp.platformVersion())
# devices = dp.deviceSerial()
# print(devices)

