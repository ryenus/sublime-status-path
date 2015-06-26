import sublime, sublime_plugin, os

class StatusPath(sublime_plugin.EventListener):
  def on_activated_async(self, view):
    # print('on_activated_async', view.file_name())
    # filename = os.path.split(view.file_name())[1]
    filename = view.file_name()
    if filename is None:
      view.erase_status('_filename')
    else:
      view.set_status('_filename', filename)
