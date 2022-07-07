#!/usr/bin/env python3

class URINorm():
  def __init__(self, uri):
    self.uri = uri

  def to_punycode(self):
    #implement rfc 3492
    uri_punycoded = self.uri.encode('idna').decode('utf-8')
    return uri_punycoded

  def remove_dot_segments(self):
    #implement rfc 3986
    prefix, _uri = URINorm(self.uri).remove_prefix(prefix=True)
    path = '/' + '/'.join(_uri.split('/')[1:])
    if len(path) == 0: return self.uri
    in_buf, out_buf = path, '' 
    while len(in_buf) != 0:
      #A
      if in_buf.startswith('../'):
        in_buf = in_buf.replace('../','',1)
      elif in_buf.startswith('./'):
        in_buf = in_buf.replace('./','',1)
      else: 
      #B
        if in_buf.startswith('/./'):
          in_buf = in_buf.replace('/./','/',1)
        elif in_buf.startswith('/.') and in_buf[2] != '.':
          in_buf = in_buf.replace('/.','/',1)
        else:
      #C
          if in_buf.startswith('/../'):
            in_buf = in_buf.replace('/../','/',1)
            last_seg = '/' + out_buf.split('/')[-1]
            out_buf = out_buf.replace(last_seg, '', -1)
          elif in_buf.startswith('/..') and in_buf[3] != '.':
            in_buf = in_buf.replace('/..','',1)
            last_seg = '/' + out_buf.split('/')[-1]
            out_buf = out_buf.replace(last_seg, '', -1)
          else:
      #D

      #E
            first_path_seg = '/' + in_buf.split('/')[1] 
            out_buf = ''.join(out_buf + first_path_seg)
            
            in_buf = in_buf.replace(first_path_seg,'')
    return prefix + _uri.split('/')[0] + out_buf 
      

  def remove_prefix(self, prefix = False):
    if self.uri.startswith('https://'): 
      if prefix == True: return 'https://', self.uri[8:]
      return self.uri[8:]
    elif self.uri.startswith('http://'): 
      if prefix == True: return 'http://', self.uri[7:]
      return self.uri[7:]
    return self.uri


