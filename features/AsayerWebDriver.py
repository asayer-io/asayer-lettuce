from lettuce import before, after, world
from selenium import webdriver
import json
import requests

with open('config/asayer.config.json') as data_file:
    CONFIG = json.load(data_file)


@before.each_feature
def setup_browser(feature):
    capabilities = CONFIG["capabilities"]

    capabilities["apikey"] = CONFIG["apikey"]
    world.apikey = CONFIG["apikey"]
    capabilities["name"] = CONFIG["name"]

    if "build" in CONFIG:
        if len(CONFIG["build"]) > 0:
            capabilities["build"] = CONFIG["build"]
        else:
            del CONFIG["build"]
    if "tunnelId" in CONFIG:
        if len(CONFIG["tunnelId"]) > 0:
            capabilities["tunnelId"] = CONFIG["tunnelId"]
        else:
            del CONFIG["tunnelId"]

    if "flags" in capabilities:
        flags = []
        for flag in capabilities["flags"]:
            flags.append(str(flag + (
                "" if isinstance(capabilities["flags"][flag], bool) and capabilities["flags"][
                    flag] else "=\"%s\"" % str(
                    capabilities["flags"][flag]))))
        capabilities["flags"] = flags
    world.requirement_id = feature.name


@before.each_scenario
def before_scenario(scenario):
    world.browser = webdriver.Remote(
        command_executor=CONFIG["server"],
        desired_capabilities=CONFIG["capabilities"]
    )
    world.session_id = world.browser.session_id


@after.each_scenario
def after_scenario(scenario):
    world.browser.quit()
    harvest_results(scenario)


def harvest_results(scenario):
    test_status = {}
    status = True
    for step in scenario.steps:
        test_status["%s: %s" % (scenario.name, step.sentence)] = "Passed" if step.passed else "Failed"
        status = status and step.passed
    mark_session_details("Passed" if status else "Failed", world.requirement_id, test_status)


def mark_session(state):
    results = {
        "sessionID": world.session_id,
        "apiKey": world.apikey,
        "sessionStatus": state
    }
    _send_results(results)


def mark_session_details(state, requirement_id, test_status):
    results = {
        "sessionID": world.session_id,
        "apiKey": world.apikey,
        "reqID": requirement_id,
        "sessionStatus": state,
        "testStatus": test_status
    }
    _send_results(results)


def _send_results(results):
    r = requests.post('https://dashboard.asayer.io/mark_session', json=results)
