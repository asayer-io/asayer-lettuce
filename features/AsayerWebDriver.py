import time
from lettuce import step, before, after, world
import lettuce_webdriver.webdriver
from selenium import webdriver
import json
from nose.tools import assert_equals

CONFIG_FILE = 'config/asayer.config.json'

with open(CONFIG_FILE) as data_file:
    CONFIG = json.load(data_file)


@before.each_feature
def setup_browser(feature):
    capabilities = CONFIG["capabilities"]
    if "flags" in capabilities:
        flags = []
        for flag in capabilities["flags"]:
            flags.append(str(flag + (
                "" if isinstance(capabilities["flags"][flag], bool) and capabilities["flags"][flag] else "=" + str(
                    capabilities["flags"][flag]))))
        capabilities["flags"] = flags
    world.browser = webdriver.Remote(
        command_executor=CONFIG["server"],
        desired_capabilities=CONFIG["capabilities"]
    )


@after.each_feature
def cleanup_browser(feature):
    print("after.each_feature")
    time.sleep(5)
    world.browser.close()
    # world.browser.quit()
