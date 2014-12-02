"""EasyEngine site controller."""

from cement.core.controller import CementBaseController, expose
from ee.core.dummy import EEDummy

class EESiteController(CementBaseController):
    class Meta:
        label = 'site'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = 'site command manages website configuration with the help of the following subcommands'
        arguments = [
            (['-f', '--foo'],
             dict(help='the notorious foo option', dest='foo', action='store',
                  metavar='TEXT') ),
            ]

    @expose(hide=True)
    def default(self):
        # TODO Default action for ee site command
        print("Inside EESiteController.default().")

    @expose(help="create site example.com")
    def create(self):
        # TODO Write code for ee site create command here
        print("Inside EESiteController.create().")

    @expose(help="delete site example.com")
    def delete(self):
        # TODO Write code for ee site delete command here
        print("Inside EESiteController.delete().")

    @expose(help="enable site example.com")
    def enable(self):
        # TODO Write code for ee site enable command here
        print("Inside EESiteController.enable().")

    @expose(help="disable site example.com")
    def disable(self):
        # TODO Write code for ee site disable command here
        print("Inside EESiteController.disable().")

    @expose(help="get example.com information")
    def info(self):
        # TODO Write code for ee site info command here
        print("Inside EESiteController.info().")

    @expose(help="Monitor example.com logs")
    def log(self):
        # TODO Write code for ee site log command here
        print("Inside EESiteController.log().")

    @expose(help="Edit example.com's nginx configuration")
    def edit(self):
        # TODO Write code for ee site edit command here
        print("Inside EESiteController.edit().")

    @expose(help="Display example.com's nginx configuration")
    def show(self):
        # TODO Write code for ee site edit command here
        print("Inside EESiteController.show().")

    @expose(help="list sites currently available")
    def list(self):
        # TODO Write code for ee site list command here
        print("Inside EESiteController.list().")

    @expose(help="change to example.com's webroot")
    def cd(self):
        # TODO Write code for ee site cd here
        print("Inside EESiteController.cd().")

    @expose(help="update example.com")
    def update(self):
        # TODO Write code for ee site update here
        print("Inside EESiteController.update().")

        # site command Options and subcommand calls and definations to
        # mention here

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
