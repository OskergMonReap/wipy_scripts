
# wifi configuration
WIFI_SSID = ''
WIFI_PASS = ''

# AWS general configuration
AWS_PORT = 8883
AWS_HOST = 'enter-endpoint-here.iot.us-east-1.amazonaws.com'
AWS_ROOT_CA = '/flash/cert/root-ca.pem'
AWS_CLIENT_CERT = '/flash/cert/public.pem.key'
AWS_PRIVATE_KEY = '/flash/cert/private.key'

################## Subscribe / Publish client #################
CLIENT_ID = 'wipyTest'
TOPIC = 'testMQTT'
OFFLINE_QUEUE_SIZE = -1
DRAINING_FREQ = 2
CONN_DISCONN_TIMEOUT = 10
MQTT_OPER_TIMEOUT = 5
LAST_WILL_TOPIC = 'testMQTT'
LAST_WILL_MSG = 'To All: Last will message'

####################### Shadow updater ########################
THING_NAME = "wipyTest"
CLIENT_ID = "ShadowUpdater"
CONN_DISCONN_TIMEOUT = 10
MQTT_OPER_TIMEOUT = 5

####################### Delta Listener ########################
THING_NAME = "wipyTest"
CLIENT_ID = "DeltaListener"
CONN_DISCONN_TIMEOUT = 10
MQTT_OPER_TIMEOUT = 5

####################### Shadow Echo ########################
THING_NAME = "wipyTest"
CLIENT_ID = "wipyTest"
CONN_DISCONN_TIMEOUT = 10
MQTT_OPER_TIMEOUT = 5
