import sublime, sublime_plugin, subprocess, os

class CmdCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if os.name == 'nt': # windows
			subprocess.Popen("cmd")
		elif os.name == 'mac' : # mac
			pass
		elif os.name == 'posix': #linux
			pass

class CmdHereCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		fname = self.view.file_name()
		path = os.sep.join(fname.split(os.sep)[:-1])
		if os.name == 'nt': # windows
			subprocess.Popen(["cmd", "/K", "cd", "/d", path])
		elif os.name == 'mac': # mac
			pass
		elif os.name == 'posix': # linux
			pass

