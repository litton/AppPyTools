#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
from google_translate import GoogleTranslate

google = GoogleTranslate()

google.read_file("/Users/litaofan/github_code/AudioRecorder/app/src/main/res/values/strings.xml")
google.start('ja')