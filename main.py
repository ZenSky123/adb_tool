import os


class Adb:
    def __init__(self, adb_path=None, serial_number=None):
        self.adb_path = adb_path if adb_path else 'adb'
        self.serial_number = serial_number

    def _execute(self, text):
        text = text.lstrip('adb ')
        if self.serial_number:
            command_template = "{adb_path} -s {serial_number} {text}"
        else:
            command_template = "{adb_path} {text}"
        command = command_template.format(
            adb_path=self.adb_path,
            serial_number=self.serial_number,
            text=text
        )
        os.system(command)

    def screenshot(self, filepath='tmp.png'):
        self._execute("exec-out screencap -p > {filepath}".format(filepath=filepath))

    def click(self, x, y):
        self._execute("shell input tap {x} {y}".format(x=x, y=y))

    def swipe(self, ax, ay, bx, by):
        self._execute('shell input swipe {ax} {ay} {bx} {by}'.format(ax=ax, ay=ay, bx=bx, by=by))

    def install(self, filepath):
        self._execute('install -r {filepath}'.format(filepath=filepath))

    def pull(self, remote, local):
        self._execute('pull {remote} {local}'.format(remote=remote, local=local))

    def push(self, local, remote):
        self._execute('push {local} {remote}'.format(local=local, remote=remote))

    def clear_log(self):
        self._execute('logcat -c')

    def wm_reset(self):
        self._execute('shell wm size reset')

    def wm_set(self, width, height):
        self._execute('shell wm size {width}x{height}'.format(width=width, height=height))
