"""List of modules that have uncaught exceptions today. Will be shrunk over time."""
IGNORE_UNCAUGHT_EXCEPTIONS = [
    ("tests.components.cast.test_media_player", "test_start_discovery_called_once"),
    ("tests.components.cast.test_media_player", "test_entry_setup_single_config"),
    ("tests.components.cast.test_media_player", "test_entry_setup_list_config"),
    ("tests.components.cast.test_media_player", "test_entry_setup_platform_not_ready"),
    ("tests.components.demo.test_init", "test_setting_up_demo"),
    ("tests.components.discovery.test_init", "test_discover_config_flow"),
    ("tests.components.dyson.test_air_quality", "test_purecool_aiq_attributes"),
    ("tests.components.dyson.test_air_quality", "test_purecool_aiq_update_state"),
    (
        "tests.components.dyson.test_air_quality",
        "test_purecool_component_setup_only_once",
    ),
    ("tests.components.dyson.test_air_quality", "test_purecool_aiq_without_discovery"),
    (
        "tests.components.dyson.test_air_quality",
        "test_purecool_aiq_empty_environment_state",
    ),
    (
        "tests.components.dyson.test_climate",
        "test_setup_component_with_parent_discovery",
    ),
    ("tests.components.dyson.test_fan", "test_purecoollink_attributes"),
    ("tests.components.dyson.test_fan", "test_purecool_turn_on"),
    ("tests.components.dyson.test_fan", "test_purecool_set_speed"),
    ("tests.components.dyson.test_fan", "test_purecool_turn_off"),
    ("tests.components.dyson.test_fan", "test_purecool_set_dyson_speed"),
    ("tests.components.dyson.test_fan", "test_purecool_oscillate"),
    ("tests.components.dyson.test_fan", "test_purecool_set_night_mode"),
    ("tests.components.dyson.test_fan", "test_purecool_set_auto_mode"),
    ("tests.components.dyson.test_fan", "test_purecool_set_angle"),
    ("tests.components.dyson.test_fan", "test_purecool_set_flow_direction_front"),
    ("tests.components.dyson.test_fan", "test_purecool_set_timer"),
    ("tests.components.dyson.test_fan", "test_purecool_update_state"),
    ("tests.components.dyson.test_fan", "test_purecool_update_state_filter_inv"),
    ("tests.components.dyson.test_fan", "test_purecool_component_setup_only_once"),
    ("tests.components.dyson.test_sensor", "test_purecool_component_setup_only_once"),
    ("tests.components.ios.test_init", "test_creating_entry_sets_up_sensor"),
    ("tests.components.ios.test_init", "test_not_configuring_ios_not_creates_entry"),
    ("tests.components.local_file.test_camera", "test_file_not_readable"),
    ("tests.components.qwikswitch.test_init", "test_binary_sensor_device"),
    ("tests.components.qwikswitch.test_init", "test_sensor_device"),
    ("tests.components.rflink.test_init", "test_send_command_invalid_arguments"),
    ("tests.components.unifi_direct.test_device_tracker", "test_get_scanner"),
]

IGNORE_UNCAUGHT_JSON_EXCEPTIONS = [
    ("tests.components.spotify.test_config_flow", "test_full_flow"),
    ("tests.components.smartthings.test_init", "test_config_entry_loads_platforms"),
    (
        "tests.components.smartthings.test_init",
        "test_scenes_unauthorized_loads_platforms",
    ),
    (
        "tests.components.smartthings.test_init",
        "test_config_entry_loads_unconnected_cloud",
    ),
]
