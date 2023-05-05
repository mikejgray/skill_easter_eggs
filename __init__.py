# pylint: disable=unused-import,missing-docstring,invalid-name
# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

import random
from os import listdir
from os.path import dirname

from adapt.intent import IntentBuilder
from ovos_workshop.skills import OVOSSkill

from .stardate import StarDate

__author__ = "jarbas"


class EasterEggsSkill(OVOSSkill):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def initialize(self):
        stardate_intent = IntentBuilder("StardateIntent").require("StardateKeyword").build()
        self.register_intent(stardate_intent, self.handle_stardate_intent)

        intent = IntentBuilder("PodBayDoorsIntent").require("PodBayDoorsKeyword").build()
        self.register_intent(intent, self.handle_pod_intent)

        intent = IntentBuilder("LanguagesYouSpeakIntent").require("LanguagesYouSpeakKeyword").build()
        self.register_intent(intent, self.handle_number_of_languages_intent)

        intent = (
            IntentBuilder("RoboticsLawsIntent")
            .require("RoboticsKeyword")
            .require("LawKeyword")
            .optionally("LawOfRobotics")
            .build()
        )
        self.register_intent(intent, self.handle_robotic_laws_intent)

        intent = (
            IntentBuilder("rock_paper_scissors_lizard_spock_Intent")
            .require("rock_paper_scissors_lizard_spock_Keyword")
            .build()
        )
        self.register_intent(intent, self.handle_rock_paper_scissors_lizard_spock_intent)

        intent = IntentBuilder("PortalIntent").require("PortalKeyword").build()
        self.register_intent(intent, self.handle_portal_intent)

        intent = IntentBuilder("DukeNukemIntent").require("DukeNukemKeyword").build()
        self.register_intent(intent, self.handle_dukenukem_intent)

        intent = IntentBuilder("HALIntent").require("HALKeyword").build()
        self.register_intent(intent, self.handle_hal_intent)

        intent = IntentBuilder("BenderIntent").require("BenderKeyword").build()
        self.register_intent(intent, self.handle_bender_intent)

        intent = IntentBuilder("ArnoldIntent").require("ArnoldKeyword").build()
        self.register_intent(intent, self.handle_arnold_intent)

        intent = IntentBuilder("GladosIntent").require("GladosKeyword").build()
        self.register_intent(intent, self.handle_glados_intent)

    def handle_stardate_intent(self, _):
        sd = StarDate().toStardate()
        self.speak_dialog("stardate", {"stardate": sd})

    def handle_pod_intent(self, _):
        self.speak_dialog("pod")

    def handle_robotic_laws_intent(self, message):
        law = str(message.data.get("LawOfRobotics", "all"))
        if law == "1":
            self.speak_dialog("rule1")
        elif law == "2":
            self.speak_dialog("rule2")
        elif law == "3":
            self.speak_dialog("rule3")
        else:
            self.speak_dialog("rule1")
            self.speak_dialog("rule2")
            self.speak_dialog("rule3")

    def handle_rock_paper_scissors_lizard_spock_intent(self, _):
        self.speak_dialog("rock_paper_scissors_lizard_spock")

    def handle_number_of_languages_intent(self, _):
        self.speak_dialog("languages")

    def handle_portal_intent(self, _):
        path = dirname(__file__) + "/sounds/portal"
        files = [mp3 for mp3 in listdir(path) if ".mp3" in mp3]
        if len(files):
            mp3 = path + "/" + random.choice(files)
            self.play_audio(mp3)
        else:
            self.speak_dialog("bad_file")

    def handle_hal_intent(self, _):
        path = dirname(__file__) + "/sounds/hal"
        files = [mp3 for mp3 in listdir(path) if ".mp3" in mp3]
        if len(files):
            mp3 = path + "/" + random.choice(files)
            self.play_audio(mp3)
        else:
            self.speak_dialog("bad_file")

    def handle_dukenukem_intent(self, _):
        path = dirname(__file__) + "/sounds/dukenukem"
        files = [wav for wav in listdir(path) if ".wav" in wav]
        if len(files):
            wav = path + "/" + random.choice(files)
            self.play_audio(wav)
        else:
            self.speak_dialog("bad_file")

    def handle_arnold_intent(self, _):
        path = dirname(__file__) + "/sounds/arnold"
        files = [wav for wav in listdir(path) if ".wav" in wav]
        if len(files):
            wav = path + "/" + random.choice(files)
            self.play_audio(wav)
        else:
            self.speak_dialog("bad_file")

    def handle_bender_intent(self, _):
        path = dirname(__file__) + "/sounds/bender"
        files = [mp3 for mp3 in listdir(path) if ".mp3" in mp3]
        if len(files):
            mp3 = path + "/" + random.choice(files)
            self.play_audio(mp3)
        else:
            self.speak_dialog("bad_file")

    def handle_glados_intent(self, _):
        path = dirname(__file__) + "/sounds/glados"
        files = [mp3 for mp3 in listdir(path) if ".mp3" in mp3]
        if len(files):
            mp3 = path + "/" + random.choice(files)
            self.play_audio(mp3)
        else:
            self.speak_dialog("bad_file")

    def stop(self):
        pass


def create_skill():
    return EasterEggsSkill()
