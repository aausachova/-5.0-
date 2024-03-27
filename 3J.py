class Device:
    devices = []
    commonUpdates = []

    def __init__(self, k, n):
        self.updates = [False] * k
        self.valueble = [0] * n
        self.requests = []
        self.countPartOfUpdates = 0
        self.nowNeedpartOfUpdate = -1
        self.iters = 0
        self.indexInDevices = len(Device.devices)
        self.myRequestOK = False
        self.idDeviceRequest = -1
        Device.devices.append(self)

    def choose_part_of_update(self):
        self.nowNeedpartOfUpdate = -1
        minCountUpdates = float('inf')
        for i in range(len(self.updates)):
            if not self.updates[i] and Device.commonUpdates[i] < minCountUpdates:
                minCountUpdates = Device.commonUpdates[i]
                self.nowNeedpartOfUpdate = i
        if self.nowNeedpartOfUpdate != -1:
            self.iters += 1

    def choose_device_who_have_part_of_update(self):
        if self.nowNeedpartOfUpdate == -1:
            return
        minDownloadUpdates = float('inf')
        deviceRequest = None
        for dev in Device.devices:
            if dev.updates[self.nowNeedpartOfUpdate]:
                if dev.countPartOfUpdates < minDownloadUpdates:
                    deviceRequest = dev
                    minDownloadUpdates = dev.countPartOfUpdates
        if deviceRequest:
            deviceRequest.requests.append(self)

    def choose_request(self):
        minCountPartOfUpdates = float('inf')
        iOkDevice = -1
        maxValueble = -1
        for dev in self.requests:
            if self.valueble[dev.indexInDevices] > maxValueble:
                iOkDevice = dev.indexInDevices
                minCountPartOfUpdates = dev.countPartOfUpdates
                maxValueble = self.valueble[dev.indexInDevices]
            elif self.valueble[dev.indexInDevices] == maxValueble:
                if minCountPartOfUpdates > dev.countPartOfUpdates:
                    iOkDevice = dev.indexInDevices
                    minCountPartOfUpdates = dev.countPartOfUpdates
        self.requests.clear()
        if iOkDevice != -1:
            dev = Device.devices[iOkDevice]
            dev.myRequestOK = True
            dev.idDeviceRequest = self.indexInDevices

    def request_OK(self):
        if not self.myRequestOK:
            return
        self.countPartOfUpdates += 1
        self.updates[self.nowNeedpartOfUpdate] = True
        Device.commonUpdates[self.nowNeedpartOfUpdate] += 1
        self.valueble[self.idDeviceRequest] += 1
        self.myRequestOK = False

def decide(n, k):
    Device.devices = []
    Device.commonUpdates = [1] * k
    for _ in range(n):
        Device(k, n)
    Device.devices[0].countPartOfUpdates = k
    Device.devices[0].updates = [True] * k
    while True:
        thisIsEnd = 0
        for dev in Device.devices:
            if dev.countPartOfUpdates == k:
                thisIsEnd += 1
                continue
            dev.choose_part_of_update()
        if thisIsEnd == n:
            break

        for dev in Device.devices:
            if dev.countPartOfUpdates == k:
                continue
            dev.choose_device_who_have_part_of_update()

        for dev in Device.devices:
            if not dev.requests:
                continue
            dev.choose_request()

        for dev in Device.devices:
            if not dev.myRequestOK:
                continue
            dev.request_OK()

    ans = [dev.iters for dev in Device.devices]
    for dev in Device.devices:
        del dev
    return ans

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        n, k = map(int, f.readline().split())

    v = decide(n, k)

    with open("output.txt", "w") as f:
        for x in v[1:]:
            f.write(str(x) + " ")
