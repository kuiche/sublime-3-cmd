import sublime, sublime_plugin, subprocess, os

class CmdCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        subprocess.Popen("cmd")

class CmdHereCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        fname = self.view.file_name()
        path = os.sep.join(fname.split(os.sep)[:-1])
        subprocess.Popen(["cmd", "/K", "cd", "/d", path])

