import os
import subprocess
class SBEngine:
    def __init__(self, app_root, bundles_root):
        self.app_root = app_root
        self.bundles_root = bundles_root
        self.bin = os.path.join(self.app_root, 'bin')
        self.plugins = os.path.join(self.app_root, 'plugins')
        self.lib = os.path.join(self.app_root, 'lib')

    def collect_data(opts=[], bundle, wait_max, event_names, end_event):
        '''
        Run and collect data until the first instance of end_event
        is found or sbengine hangs for wait_max seconds, whichever 
        comes first. 

        Returns a list of events
        '''
        events = []
        sbengine = os.path.join(self.bin, 'sbengine')
        # Add verbosity arg to sbengine
        opts.append('-vvvv')
        # Set necessary env
        os.environ['SB_PLUGINS'] = self.plugins
        os.environ['LD_LIBRARY_PATH'] = self.lib

        bundle = os.path.join(self.bundles_root, bundle) + '.gapp'

        # Build command string to be executed
        args = []
        args.append(sbengine)

        cmd = f'{sbengine} {opts} {bundle}'

        # Run command as a subprocess
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
