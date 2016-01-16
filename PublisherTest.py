#!/usr/bin/env python
# -*- coding: euc-jp -*-




import OpenRTM_aist


class PublisherTest(OpenRTM_aist.PublisherBase):
 
  def __init__(self):
    self._consumer  = None
    self._active    = False
    self._profile   = None
    self._listeners = None
    self._retcode   = self.PORT_OK

 
  def __del__(self):
    self._consumer = None
    return

  def init(self, prop):
    return self.PORT_OK

  def setConsumer(self, consumer):
    if not consumer:
      return self.INVALID_ARGS

    self._consumer = consumer

    return self.PORT_OK

  def setBuffer(self, buffer):
    return self.PORT_OK

  def setListener(self, info, listeners):
    
    if not listeners:
      return self.INVALID_ARGS

    self._profile = info
    self._listeners = listeners

    return self.PORT_OK

  def write(self, data, sec, usec):
    self._retcode = self._consumer.put(data)
    self._retcode = self._consumer.put(data)

    return self._retcode

  def isActive(self):
    return self._active

  def activate(self):
    if self._active:
      return self.PRECONDITION_NOT_MET

    self._active = True

    return self.PORT_OK

  def deactivate(self):
    if not self._active:
      return self.PRECONDITION_NOT_MET

    self._active = False

    return self.PORT_OK

  

def PublisherTestInit(manager):
  OpenRTM_aist.PublisherFactory.instance().addFactory("test",
                                                      PublisherTest,
                                                      OpenRTM_aist.Delete)
