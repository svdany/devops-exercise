import sys
import yaml
import tornado.ioloop, tornado.web

class Server(object):
  def __init__(self,config):
    # Setup url handler and initialize the server
    self.config = config
    urls = [
      ('/(.*)', tornado.web.StaticFileHandler, {'path': self.config['resources']})
    ]

    app = tornado.web.Application(urls)
    app.listen(int(self.config['port']))

  def start(self):
    print 'Server starting on port %s' % (self.config['port'])
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
  #Do some basic error checking and start the server
  if len(sys.argv) > 1:
    try:
      fh = open(sys.argv[1])
      config = yaml.load(fh.read())
    except:
      print 'Something is wrong with config file'

    Server(config).start()
  else:
    print 'No config file specified'
