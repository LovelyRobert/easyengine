from cement.core.controller import CementBaseController, expose
from cement.core import handler, hook
from ee.core.services import EEService


class EEStackStatusController(CementBaseController):
    class Meta:
        label = 'stack_services'
        stacked_on = 'stack'
        stacked_type = 'embedded'
        description = 'stack command manages stack operations'
        arguments = [
            (['--memcache'],
                dict(help='start/stop/restart stack', action='store_true')),
            (['--dovecot'],
                dict(help='start/stop/restart dovecot', action='store_true')),
            ]

    @expose(help="start stack services")
    def start(self):
        services = []
        if self.app.pargs.nginx:
            services = services + ['nginx']
        elif self.app.pargs.php:
            services = services + ['php5-fpm']
        elif self.app.pargs.mysql:
            services = services + ['mysql']
        elif self.app.pargs.postfix:
            services = services + ['postfix']
        elif self.app.pargs.memcache:
            services = services + ['memcached']
        elif self.app.pargs.dovecot:
            services = services + ['dovecot']
        else:
            services = services + ['nginx', 'php5-fpm', 'mysql', 'postfix']
        for service in services:
            EEService.start_service(service)

    @expose(help="stop stack services")
    def stop(self):
        services = []
        if self.app.pargs.nginx:
            services = services + ['nginx']
        elif self.app.pargs.php:
            services = services + ['php5-fpm']
        elif self.app.pargs.mysql:
            services = services + ['mysql']
        elif self.app.pargs.postfix:
            services = services + ['postfix']
        elif self.app.pargs.memcache:
            services = services + ['memcached']
        elif self.app.pargs.dovecot:
            services = services + ['dovecot']
        else:
            services = services + ['nginx', 'php5-fpm', 'mysql', 'postfix']
        for service in services:
            EEService.stop_service(service)

    @expose(help="restart stack services")
    def restart(self):
        services = []
        if self.app.pargs.nginx:
            services = services + ['nginx']
        elif self.app.pargs.php:
            services = services + ['php5-fpm']
        elif self.app.pargs.mysql:
            services = services + ['mysql']
        elif self.app.pargs.postfix:
            services = services + ['postfix']
        elif self.app.pargs.memcache:
            services = services + ['memcached']
        elif self.app.pargs.dovecot:
            services = services + ['dovecot']
        else:
            services = services + ['nginx', 'php5-fpm', 'mysql', 'postfix']
        for service in services:
            EEService.restart_service(service)

    @expose(help="get stack status")
    def status(self):
        pass
