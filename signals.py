import django.dispatch

sendgrid_email_sent = django.dispatch.Signal(providing_args=["message", "response"])
sendgrid_event_recieved = django.dispatch.Signal(providing_args=["request"])
sendgrid_event_created = django.dispatch.Signal(providing_args=["request", "event"])
