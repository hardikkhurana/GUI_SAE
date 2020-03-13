import dash_daq as daq

daq.Gauge(
  id='my-daq-gauge',
  value=6,
  min=0,
  max=10
)