AYLA_USER_SERVERS = {
    'us': 'user-field.aylanetworks.com',
    'eu': 'user-field-eu.aylanetworks.com',
    'cn': 'user-field.ayla.com.cn',
}
AYLA_DEVICES_SERVERS = {
    'us': 'ads-field.aylanetworks.com',
    'eu': 'ads-eu.aylanetworks.com',
    'cn': 'ads-field.ayla.com.cn',
}
SECRET_MAP = {
    'oem-us':
        b'\x1dgAPT\xd1\xa9\xec\xe2\xa2\x01\x19\xc0\x03X\x13j\xfc\xb5\x91',
    'mid-us':
        b'\xdeCx\xbe\x0cq8\x0b\x99\xb4Z\x93>\xfc\xcc\x9ag\x98\xf8\x14',
    'tornado-us':
        b'\x87O\xf2.&;X\xfb\xf6L\xfdRq\'\x0f\t6\x0c\xfd)',
    'wwh-us':
        b'(\xcb9w\xc5\xc9\xb7\xab{*k8T!Yb\xaa\xcf\xd0\x85',
    'winia-us':
        b'\xeb_\xce\xb2\xc6\xff`\xa9\xfa\xa8r\x1c\x0bH\xf8\xe27\xa7U\xec',
    'york-us':
        b'\xc6A\x7fHyV<\xb2\xa2\xde<\x1f{c\xa9\rt\x9fy\xef',
    'beko-eu':
        b'\xa9C\n\xdb\xf7+\x01\xe2X\ne\x85\x06\x89\xaa\x88ZP+\x07>~s{\xd3\x1f\x05\x91&\x8c\x81\x84&\xe11\xef=s"*\xa4',
    'oem-eu':
        b'a\x1ez\xf5\xc4\x0f\x18~\xe5\xeb\xb1\x9f\xe4\xf5&B\xfe#\x88\xcb>\x06O,y\xc1\x06c\x9d\x99J\xc2x\xac\xeb\x82\x93\xe5\r\x89d',
    'mid-eu':
        b'\x05$\xe6\xecW\xa3\xd1B\xa0\x84\xab*\xf0\x04\x80\xce\xae\xe5`\xc4>w\xf8\xc4\xf3X\xf6<\xd2\xd2I\x14!\xd0\x98\xed\xf2\xab\xae\xc6\x03',
    'haxxair':
        b'\xd8\xaf\x89--\x00\xabI\x93\x83j\xab\x9acX\xac^\x90f;',
    'fglair-cn':
        b'\xcd\xec\xe0\xed\x8e\xb4b\x90/\xcbq\xcf\xc3\x1b\xd6.wx:\x1e',
    'fglair-eu':
        b'\x82\x91[T\x14h\x88\x9f\x04\xdd\x05\x89\xf9\x04T,\xb2\xf7\x8fu',
    'fglair-us':
        b'U\xbf\x0c@\xbf\xe5\x16&\x10\xec2\xa37G\x82\x15|\xe7)\x91',
    'field-us':
        b'\xc8b\x08\xfa\xce8\xf8\xf1\x81\xa5\x81\x8fX\xb4\x80\xc0\xdc\xf5\ny',
    'huihe-us':
        b'\xa2\xbcZ3\xbch\xfa7.`\xbc\xef0\xa3p\xa1\xf0\xaf\xf4\xd4',
    'denali-us':
        b'\xf1\'\xb0K \xdbZ\xd84;\xeb\x02\xa2\xee\x008\xda\x95\xfd\x93',
    'hisense-eu':
        b'\xc0\xedK,\xff+X\xfa\xf6p\x87\xaa\xbcV\x88\xfbI\xb4\xcf\xad',
    'hisense-us':
        b'x\x04\xdf\xef6\x08\x8e\x06\n\x97\xfc\xed4m\xd8\xc7\xa3=\xce\x9f',
    'hismart-eu':
        b'0\x07\xe9\x04a\xa6e\xc4\x1c\x08+"\r\x84w\x91\x8f\xa8)\x98',
    'hismart-us':
        b'\xd6+\x1f\xb0b\t\x19G\x87\x8c\xaak\xd0\xf8y\xf5\x933\xafp',
}
SECRET_ID_MAP = {
    'haxxair': 'HAXXAIR',
    'field-us': 'pactera-field-f624d97f-us',
    'fglair-cn': 'FGLairField-cn',
    'fglair-eu': 'FGLair-eu',
    'fglair-us': 'CJIOSP',
    'huihe-us': 'huihe-d70b5148-field-us',
    'denali-us': 'DenaliAire',
    'hisense-eu': 'Hisense',
    'hisense-us': 'APP1',
    'hismart-eu': 'Hismart',
    'hismart-us': 'App1',
}
SECRET_ID_EXTRA_MAP = {
    'denali-us': 'iA',
    'hisense-eu': 'mw',
    'hisense-us': 'pg',
    'hismart-eu': 'fA',
    'hismart-us': 'Lg',
}
# Most ACs are using Fahrenheit in their API. These do not:
CELSIUS_BASED_APPS = {'fglair-eu', 'hisense-eu', 'hisense-us', 'hismart-eu'}
