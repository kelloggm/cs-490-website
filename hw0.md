---
layout: project
title: "Homework 0: Setup"
permalink: /projects/hw0.html
parent: Homeworks
nav_order: 1
due_date: "Wednesday, January 24, 2024, 11:59PM AoE"
submission_notes: Submit via Canvas
---

CS 684 is a software engineering course. There a focus on reading code and using large systems to accomplish tasks,
because real systems are large---too large for you to hold their entire specification or codebase in your head,
almost certainly.
In this course, you will be expected to develop and maintain programs
and scripts in multiple languages using multiple tools.
As a result, I want to help you prepare a suitable development environment for the assignments in this course.
Creating a Virtual Machine may be useful for the assignments in this class. HW0 will guide you in doing just that.

**This assignment will help you create a development environment that matches the autograder environment.**
If you are not familiar with Linux command line tools, this assignment is a great place to start.

The assignments in this course have been designed around an x86\_64
Ubuntu 22.04 LTS environment.  All of the assignments are known to
work in this environment. Officially, you _have_ to use this
environment. (If you do not then you will likely run into issues that
are not covered in the homework specifications. That is, later
commands will not work for you and you will be unable to complete the
homeworks.) Different versions of tools and libraries are installed by
default in different versions of Linux. As a result, if you deviate
from the suggested x86\_64 Ubuntu 22.04 environment, you may encounter
corner cases that cause test cases to fail on the autograder. In some
cases, the staff may direct you to set up an Ubuntu 22.04 Virtual
Machine if you have not done so and are stuck on some
assignments. Ultimately, it is _your responsibility_ to read
documentation and install supported tools. This HW0 spec is meant to
help you walk through the creation of an x86\_64 Ubuntu 22.04
environment.

## Two Options — Local or Cloud

You must select _one_ of the following two full-credit options for this assignment:
1. **Option 1: Local**: Set up a local Ubuntu 22.04 Virtual machine on your computer. _This is the most popular option for most students._ It has a nice UI that makes it easy to navigate.
* Some students may have WSL Ubuntu set up. Unfortunately, it is a different version of Ubuntu and may not work for this class: we recomend that you follow the instructions below. However, your experience setting it up will help you here!
* Some student reports that VirtualBox is not compatible with the new Macbooks (e.g., with M1 and M2 chipsets). If you are using such a Macbook, you may have to select the Option 2 below and use the Cloud instead of your local machine.
* Some students may be tempted to install an ARM Ubuntu setup, but unfortunately the x86\_64 architecture is required. (If you're not certain what this means, you can ignore it.)
* Some students have experience with docker. Unfortunately, docker will not suffice here (but experience with it will help you): follow the instructions below.
* Some students already have other versions of Ubuntu installed. Crushingly, you will almost certainly need the specific version mentioned here: follow the instructions below.
2. **Option 2: Cloud**: Set up an Amazon EC2 cloud instance with Ubuntu 22.04 running on it. This option will work if you have a slower or older computer. _Start early; Amazon takes up to 24 hours to verify cloud computing accounts._ This option involves more of a command-line interface but typically runs some course tools a bit faster than local machine.

Both options should work with all assignments in this course. Option 1 (local VM) will have you install VirtualBox on your computer, download an Ubuntu 22.04 installation image, and install x86\_64 Ubuntu 22.04 in your virtual machine. A reasonably modern computer (e.g., at most 5 years old) should be able to run a VM guest without issue. However, some students report that the VM executes too slowly (e.g., the mouse is laggy, keystrokes are missed, programs take too long, etc.). If your VM guest is too slow, you can consider using Option 2 instead (see below).

First, you may want to read the summary of virtual machines and cloud computing below. Even if you are familiar with the concepts from previous experiences, this course may use slightly different terminology, and I recommend that you skim the material (click on the box below to see the background material).

<details markdown="block">
  <summary>
    Background: Virtual Machines and Cloud Computing
  </summary>

A [Virtual Machine](https://en.wikipedia.org/wiki/Virtual_machine) is an emulation of a computer system. Loosely, you
can think of a VM as a program that can run an entire virtual computer
system. Virtual machines are powerful software systems that enable
running software designed for one operating system inside another
operating system.

For example, you can use your Windows host computer to run a Virtual Machine that contains a Linux operating system. Consider the image below:

![](../assets/vms.png)

This is a Windows 10 _host_computer running three different Virtual Machine _guests_.
The guest instances are complete (virtual) environments that are isolated from the host. All of the guests share the host's hardware as they execute — each window in the screenshot above lets you interact with a separate emulated guest.

Thus, even though the host is a Windows computer, you can use one of the guests to execute Linux software inside the guest. Virtual Machines can be used in many combinations. You can have a Windows, Linux, or Mac host computer, and run arbitary numbers and combinations of Linux and Windows guests. Finally, guests are stored as files in the host computer — this means you can move your VM guest from one host to another by transferring that file around.

*Option 1 ("Local")*: You can choose to set up and run your own Ubuntu 22.04 virtual machine locally. This will allow you complete all of the assignments in this course within that virtual machine. However, some students report that the VM guest runs too slowly (especially if you do not have enough RAM in your computer). If you find that a local VM is too slow, you can use _Option 2_ instead.

Virtual machines are a critical part of [Cloud computing](https://en.wikipedia.org/wiki/Cloud_computing). You can "rent out" computing resources from a provider like Amazon EC2 or Microsoft Azure to do whatever computation you might need. Amazon EC2 and Microsoft Azure both offer you _virtual machine guests_ that run on their hardware. Thus, you can get access to a virtual machine running whatever operating system you like to run a variety of software.

*Option 2 ("Cloud")*: If you find that a local VM is too slow, you can instead get a free Ubuntu 22.04 virtual machine from [Amazon EC2](https://aws.amazon.com/ec2/) (or any other cloud computing provider, but this specification walks you through how to do it on EC2). Amazon EC2 ("<ins>E</ins>lastic <ins>C</ins>loud <ins>C</ins>ompute") is a service that lets you buy and configure virtual machines. Option 2 has you setup and launch an Ubuntu 22.04 cloud instance (this is free if you are a student).

</details>

Many of the assignments are easier to complete on Linux or similar command-line systems. If you're not
comfortable with such systems, the background tab below on Linux Fundamentals might be useful:

<details markdown="block">
<summary>Background: Linux Fundamentals</summary>

Vanderbilt professor [Kevin Leach](https://kjl.name/) has prepared a (long) video that provides a gentle introduction to a number of Linux concepts that are relevant to this course. This video is optional, but you may find it useful if you are less familiar with the Linux environment.

<iframe width="400" height="300"
src="https://www.youtube.com/embed/IgqDbq0mzJ0">
</iframe>

There are timestamps in a comment below the video that contain points of interest, such as:
* terminals
* environment variables
* scripts in the shell
* compiling programs from source
* using ssh

The first half is more about terminals and shells (why do we have to
type `./a.out`? why can't we just say `a.out`?), and the second half is
more about compiling programs from source. The video also covers
`elinks` in particular, which is a terminal-based browser program
(using `elinks` is not required for this course, but it might be helpful
if you choose to use a cloud computer and need to access the web to e.g.,
submit an assignment).

</details>

## Option 1 — Local Virtual Machine

You can set up your own local virtual machine for free. However, before you proceed, consider checking whether your CPU supports accelerated virtualization. If your CPU does not support virtualization extensions, then your VM may run slowly. If that's the case, consider Option 2 for this assignment instead.

You will need:

* A copy of VirtualBox for your operating system. [General download link (look under "Platform Package" or similar)](https://www.virtualbox.org/wiki/Downloads).
* A copy of 64-bit Ubuntu 22.04 ([Download](https://releases.ubuntu.com/jammy/) — 64-bit is required here: don't use 32-bit). This is a large `.iso` file that might take a long time to download. You don't need it until part way through the installation process, but you should start the download now.
* When something goes wrong during this installation, we recommend that you _search this webpage_ and aslo _look for previous posts on the forum_. Some solutions may be listed a little lower on the webpage than when you encounter them. Macs typically give students many more issues than Windows machines, so if you are a student using a Mac, looking to see if the issue is already addressed can be a big time saver.

### VirtualBox

VirtualBox is a _Virtual Machine Manager_. You install VirtualBox on your host computer (i.e., as a regular program or app). Then, you use VirtualBox to create a virtual machine guest. Once you have created a guest, you install Ubuntu 22.04 inside of the guest. Then, you can start the guest and have a complete Ubuntu 22.04 environment within that guest.

<details markdown="block">

<summary>Isolation in Virtual Machine Guests</summary>

Note well: Implicit here is that the guest is, to some extent, _isolated_ from the host. This is very important and entails a number of conceptual hurdles if you are not used to virtualization:
* The clipboard is isolated. That is, if you copy something from your host environment, you cannot paste it inside the guest environment. This is because the VM guest is a completely independent operating system environment from your host.
* Typing and mouse movements have to be captured by the guest.
* If you want to download a file to use in the guest, you must do so from the guest environment. Unless you set up a shared drive (which is not required), you have to download or create files within the guest environment rather than the host environment.

</details>

### Installing VirtualBox

You can install VirtualBox with the default settings. For your reference, screenshots of the course staff completing the installation are shown below:

![](../assets/install1.png)
![](../assets/install2.png)

If you receive a "The installation failed." message on a Mac, you can resolve the issue by going to Security and Privacy and allowing the installation.

## Creating a Virtual Machine

After installing VirtualBox, it will display the main VM Management console, which we can use to create a New Machine (see circular highlight in upper left):

![](../assets/create-vm1.png)

Next, configure your virtual machine. Select "Type" as "Linux" and "Version" as "Ubuntu 64-bit". (If you only see options for 32-bit and do not see options for 64-bit, you will not be able to complete this option and will instead have to use the Amazon EC2 Cloud instance option. This happens to some students with older 32-bit Mac machines that cannot emulate 64-bit guests.) You can name your VM whatever you like (though note that the name in the picture is from a different course than this one that uses the same setup). We recommend using at least 2048MB of Memory. See highlights below:

![](../assets/create-vm2.png)

Next, it will ask you to create a storage device. Remember, you are creating a virtual machine — an entire simulated computer. That includes simulating a hard disk for storage. This is represented as a large (> 20GB file) on your host computer. We recommend at least 20GB, and you can choose "dynamically allocated" to save space:

![](../assets/create-vm3.png)

After this step, you will have successfully created a Virtual Machine. Now, you have a bare system with nothing installed on it. Next, we must install an OS on it to run the VM.

## Installing an OS in the Guest VM

After creating a VM, we need to install Ubuntu 22.04 on it to help run software. Remember downloading a large `.iso` file as indicated above when we discussed downloading Ubuntu (if you missed it, you should go back and download it now)? This is a _Disk Image_ — we need to attach the OS Disk Image into the VM.

On the VM Management window, right click the VM you just created, and click "Settings":

![](../assets/create-vm4.png)

Next, click on "Storage", then click on the "Empty IDE Controller" (your version of VirtualBox may call this a CD drive, Optical storage drive, or similar. Regardless, you should be able to select a virtual disk image). Click the Disk icon, then click "Choose disk file...":

![](../assets/create-vm5.png)

Then, select the Ubuntu `.iso` file you downloaded earlier. This places the Ubuntu 22.04 installation medium in the VM's disk drive. Click OK, and you are now ready to start your VM from the Manager (note: the image below is from a previous version of the course that used Ubuntu 16.04 instead of Ubuntu 22.04. When you do this, your `.iso` file must be for Ubuntu 22.04.):

![](../assets/create-vm6.png)

If you receive a "Kernel driver not installed" error, follow [these instructions online](https://www.howtogeek.com/658047/how-to-fix-virtualboxs-%E2%80%9Ckernel-driver-not-installed-rc-1908-error/) for how to resolve the issue. (The image below shows the "Kernel driver not installed" error, for your reference.)

![](../assets/hw0-mac-kernel.png)

The Virtual Machine will now boot and load the Ubuntu 22.04 installation. The VM opens in a new window — you can think of this window as the virtual "screen" that lets you see what's happening in the emulated system. You can follow through the normal Ubuntu 22.04 installation:

![](../assets/create-vm7.png)

*Note*: If the VM asks you to select a startup disk, you need only select your `.iso` file. You want the VM to boot from the installation media so you can install Ubuntu within the guest.

We recommend opting to install updates and third-party software. It should not affect the system one way or another:

![](../assets/create-vm8.png)

You can select "Erase disk and install Ubuntu". This is only referring to erasing the "virtual" disk you created earlier with the VM.

![](../assets/create-vm9.png)

If you are receiving an error like the "following disc images couldn't be opened for the reason of no mountable file systems", you may be able to resolve the issue by following [recommendations online](https://deciphertools.com/blog/2017-10-02-no-mountable-file-systems/)

Note: Sometimes during installation, students find that a window is too large to display all the buttons. You can actually move the window like normal to reveal the Continue button (just click to drag the window like any other — the window inside the Virtual Machine, not the Virtual Machine itself):

![](../assets/create-vm10.png)

Next, it will ask you to create an account for logging in. You can put whatever credentials you like here — it will not have any bearing on your host computer. This is merely for an account on the guest VM. Just make sure you don't forget whatever password you choose!

![](../assets/create-vm11.png)

Next, you just wait a bit for the OS to install inside the guest. It might take a few minutes to complete. Eventually, you'll see a screen asking you to remove installaton media and restart. You can just click restart (on the guest) and you'll be all set!

<details markdown="block">
<summary>Virtual Machines and Mice</summary>
While you're running the VM, you may find that it "takes control" of your mouse and keyboard, and you aren't able to leave the window. If this happens, press CTRL+ALT to release control from the VM window. (The keystrokes may be different on Mac OS).
</details>

## Install VirtualBox Additions

One thing you'll notice when you install your VM successfully is that the window is small. In our opinion, one thing that makes the experience way better is the VirtualBox Additions package. It provides a number of "Quality of Life" features when using VMs. It's essentially a helper program you install inside the VM guest that makes it "aware" that it's running inside of a VM. To install, click "Devices", then "Insert Guest Additions CD Image..."

![](../assets/create-vm15.png)

Eventually, a window pops up asking if you want to run the media. Just click Run.

![](../assets/create-vm16.png)

After installing, you can reboot the VM image. One more step to make sure `gcc` (a compiler for C and C++ programs) is installed in your guest. In a terminal, use:

```
sudo apt-get update
sudo apt-get install gcc
```

You're all set! You can proceed to submitting the assignment (see below, after option 2)!

## Option 2 — Amazon EC2

