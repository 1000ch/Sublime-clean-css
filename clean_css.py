import sublime
import sublime_plugin
import json
from os.path import dirname, realpath, join

try:
    # Python 2
    from node_bridge import node_bridge
except:
    from .node_bridge import node_bridge

sublime.Region.totuple = lambda self: (self.a, self.b)
sublime.Region.__iter__ = lambda self: self.totuple().__iter__()

BIN_PATH = join(sublime.packages_path(), dirname(realpath(__file__)), 'clean-css.mjs')

def get_setting(view, key):
    settings = view.settings().get('Clean-css')

    if settings is None:
        settings = sublime.load_settings('Clean-css.sublime-settings')

    return settings.get(key)

class CleanCssFormatCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        region = sublime.Region(0, self.view.size())
        buffer = self.view.substr(region)
        processed = self.format(buffer)

        if processed:
            self.view.replace(edit, region, processed)

    def format(self, data):
        try:
            return node_bridge(data, BIN_PATH, [json.dumps({
                'compatibility': get_setting(self.view, 'compatibility'),
                'level': get_setting(self.view, 'level'),
                'format': get_setting(self.view, 'format'),
                'inline': get_setting(self.view, 'inline')
            })])
        except Exception as e:
            sublime.error_message('clean-css\n%s' % e)

class CleanCssMinifyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        region = sublime.Region(0, self.view.size())
        buffer = self.view.substr(region)
        processed = self.minify(buffer)

        if processed:
            self.view.replace(edit, region, processed)

    def minify(self, data):
        try:
            return node_bridge(data, BIN_PATH, [json.dumps({
                'compatibility': get_setting(self.view, 'compatibility'),
                'level': get_setting(self.view, 'level'),
                'inline': get_setting(self.view, 'inline')
            })])
        except Exception as e:
            sublime.error_message('clean-css\n%s' % e)
