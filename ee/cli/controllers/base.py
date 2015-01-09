"""EasyEngine base controller."""

from cement.core.controller import CementBaseController, expose


class EEBaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = 'easyengine is the commandline tool to manage your \
                        websites based on wordpress and nginx with easy to \
                        use commands.'
        arguments = [
            (['-f', '--foo'],
             dict(help='the notorious foo option', dest='foo', action='store',
                  metavar='TEXT')),
            ]

    @expose(hide=True)
    def default(self):
        data = dict(foo='EEBaseController.default().')
        self.app.render((data), 'default.mustache')

        # print("Inside EEBaseController.default().")

        # If using an output handler such as 'mustache', you could also
        # render a data dictionary using a template.  For example:
        #
        #   data = dict(foo='bar')
        #   self.app.render(data, 'default.mustache')
        #
        #
        # The 'default.mustache' file would be loaded from
        # ``ee.cli.templates``, or ``/var/lib/ee/templates/``.
        #
        # ViMbAdmin Nginx configuration
        data = dict(site_name='webmail', www_domain='webmail', static=False,
                    basic=True, wp=False, w3tc=False, wpfc=False,
                    wpsc=False, multisite=False, wpsubdir=False,
                    webroot='/var/www', ee_db_name='',
                    ee_db_user='', ee_db_pass='', ee_db_host='',
                    rc=True)
        self.app.log.debug('Writting the nginx configration for'
                           ' ViMbAdmin')
        ee_rc = open('/etc/nginx/sites-available/webmail.conf', 'w')
        self.app.render((data), 'virtualconf.mustache',
                        out=ee_rc)
        ee_rc.close()
