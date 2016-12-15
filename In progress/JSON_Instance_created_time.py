{
	'ResponseMetadata': {
		'HTTPStatusCode': 200,
		'RequestId': '6e051d49-3a07-4a67-8a37-cf19927ecfc3',
		'HTTPHeaders': {
			'transfer-encoding': 'chunked',
			'vary': 'Accept-Encoding',
			'server': 'AmazonEC2',
			'content-type': 'text/xml;charset=UTF-8',
			'date': 'Fri, 02 Dec 2016 05:57:37 GMT'
		}
	},
	u 'Volumes': [{
		u 'AvailabilityZone': 'us-west-2a',
		u 'Attachments': [{
			u 'AttachTime': datetime.datetime(2016, 10, 20, 8, 33, 53, tzinfo = tzlocal()),
			u 'InstanceId': 'i-0db9fb9bbe6704953',
			u 'VolumeId': 'vol-00adb7613f34a4e92',
			u 'State': 'attached',
			u 'DeleteOnTermination': True,
			u 'Device': '/dev/xvda'
		}],
		u 'Encrypted': False,
		u 'VolumeType': 'gp2',
		u 'VolumeId': 'vol-00adb7613f34a4e92',
		u 'State': 'in-use',
		u 'Iops': 100,
		u 'SnapshotId': 'snap-c87f35ec',
		u 'CreateTime': datetime.datetime(2016, 10, 20, 8, 33, 53, 886000, tzinfo = tzlocal()),
		u 'Size': 20
	}]
}