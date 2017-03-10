#coding=utf8
#!/etc/bin/python 


import re
import json
import urlparse
import os

from datetime import datetime

class LogParser():
    def __init__(self):
        pass

    def _test_file(self):
        return os.path.exists(os.path.abspath(file_name))

    def test_line(self, line, pattern_str):
        try:
            return re.search(re.compile(pattern_str), line)
        except:
            return False

    def get_string_from_records(self, str, head_str, tail_str, head_included=True, tail_included=True):

        head, tail = str.index(head_str), str.index(tail_str)
        head_index = head if head_included else head + len(head_str)
        tail_index = tail + len(tail_str) if tail_included else tail 
        target = str[head_index:tail_index]
        return target

    def slice_json_object_from_string(self, str, head, tail):

        raw_obj = str[head:tail+1]
        return json.loads(raw_obj)

    def get_time_stamp(self, time_str, time_pattern):
        time_stampe = datetime.strptime(time_str, time_pattern)
        return time_stampe

    def _get_all_index(self, str, target_str):
        return [each.start() for each in re.finditer(target_str, str)]

    def _get_parsed_url(self, url, target='hostname'):
        url_obj = urlparse.urlparse(url)
        if target== 'hostname':
            return url_obj.hostname
        elif target == 'path':
            return url_obj.path
        elif target == 'port':
            return url_obj.port
        else:
            return url_obj

    def get_json_object(self, raw_str, head, tail):
        # head, and tail should be just '{','}', '[', ']'
        stack = []

        for k, c in enumerate(raw_str):
            if c == head:
                stack.append(k)
            elif c == tail:
                if len(stack) == 1:
                    yield self.slice_json_object_from_string(raw_str, stack[0], k)
                    stack.pop()
                else:
                    stack.pop()

        yield None


class LogStats():
    def __init__(self, stats_dict):
        pass
