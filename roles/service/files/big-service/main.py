import sys
import yaml
import tornado.ioloop, tornado.web



class RequestCountHandler(tornado.web.RequestHandler):
  COUNTER=0 # Static class var
  def get(self):
    #Increment the counter and write the repsponse
    RequestCountHandler.COUNTER+=1
    self.write(str(RequestCountHandler.COUNTER))

class Server(object):
  def __init__(self,config):
    # Setup url handlers and initialize the server
    self.config = config
    urls = [
      ('/',RequestCountHandler)
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
