#!/usr/bin/env python3

import emails
import psutil, shutil, socket
import os

disk_data = psutil.virtual_memory()

def cpu_check():
	if psutil.cpu_percent(1) > 80:
		return True

def disk_space_check():
	if disk_data.free/disk_data.total < 0.20:
		return True

def check_av_mem():
	free = disk_data.free>>20
	if free < 500:
		return True

def hostname_check():
  local_host_ip = socket.gethostbyname('localhost')
  return local_host_ip != "127.0.0.1"

def email_warning(error):
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ["USER"])
  subject = error
  body = "Please check your system and resolve the issue as soon as possible."
  message = emails.generate_email(sender, receiver, subject, body)
  emails.send_email(message)

if cpu_check():
	subject = 'Error - CPU usage is over 80%'
	email_warning(subject)

if disk_space_check():
  subject = "Error - Available disk space is less than 20%"
  email_warning(subject)

if check_av_mem():
  subject = "Error - Available memory is less than 500MB"
  email_warning(subject)

if hostname_check():
  subject = "Error - localhost cannot be resolved to 127.0.0.1"
  email_warning(subject)
