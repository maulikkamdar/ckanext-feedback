import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class FeedbackPlugin(plugins.SingletonPlugin):
  plugins.implements(plugins.IConfigurer)
  plugins.implements(plugins.IRoutes, inherit=True)

  def update_config(self,config):
    toolkit.add_template_directory(config, 'templates')

  def before_map(self, m):
    m.connect('feedback', '/feedback', controller='ckanext.feedback.controller:FeedbackController', action='feedback')
    m.connect('feedbackProv', '/feedbackProv', controller='ckanext.feedback.controller:FeedbackController', action='feedbackProv')
    return m

