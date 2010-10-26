# Universal Subtitles, universalsubtitles.org
# 
# Copyright (C) 2010 Participatory Culture Foundation
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see 
# http://www.gnu.org/licenses/agpl-3.0.html.

from urlparse import urlparse

class VideoType(object):
    
    def __init__(self):
        self.abbreviation = None
        self.name = None        
    
    def matches_video_url(self, url):
        raise Exception('Not implemented')
    
    def video_url(self, obj):
        raise Exception('Not implemented')
    
    @property
    def defaults(self):
        return {
            'video_type': self.abbreviation,
            'allow_community_edits': True
        }
    
    def create_kwars(self):
        raise Exception('Not implented')
    
    def set_values(self, video_obj, video_url):
        return video_obj

    def format_url(self, url):
        parsed_url = urlparse(url)
        return '%s://%s%s' % (parsed_url.scheme or 'http', parsed_url.netloc, parsed_url.path)    
    
class VideoTypeRegistrar(dict):
    
    def __init__(self, *args, **kwargs):
        super(VideoTypeRegistrar, self).__init__(*args, **kwargs)
        self.choices = []
        
    def register(self, video_type):
        self[video_type.abbreviation] = video_type
        self.choices.append((video_type.abbreviation, video_type.name))

    def video_type_for_url(self, url):
        for video_type in self.values():
            if video_type.matches_video_url(url):
                return video_type      