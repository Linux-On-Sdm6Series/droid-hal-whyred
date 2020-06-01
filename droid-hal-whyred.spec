%define device whyred
%define vendor xiaomi
%define vendor_pretty Xiaomi
%define device_pretty Redmi Note 5
%define installable_zip 1
%define droid_target_aarch64 1

# want adreno quirks is required for browser at least, and other subtle issues
%define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}

%define straggler_files \
  /acct \
  /bugreports \
  /bt_firmware \
  /cache \
  /charger \
  /d \
  /dsp \
  /firmware \
  /odm \
  /oem \
  /persist \
  /product \
  /sdcard \
  /storage \
%{nil}

# System as Root
%define makefstab_skip_entries / /vendor /dev/stune /dev/cpuset /sys/fs/pstore /dev/cpuctl

%include rpm/dhd/droid-hal-device.inc
