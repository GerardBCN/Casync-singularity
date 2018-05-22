## Casync-singularity

Casync-singularity aims to containerize the Casync tool and make it executable. Casync repo can be found in https://github.com/systemd/casync.
Casync is a tool that can be used for efficiently updating SquashFS images through HTTP, for instance produced by singularity. 

The typical use case addressed here includes the following components:

**(a)** we have a remote server where we store squashfs images. 
**(b)** we have a local server, where we constinuosly change, update and re-build the images.

The objective is that we can update the images in the remote server in an efficient way without having to transfer the whole image file, which can of several gigabytes, e.g. up to 10 GB. 

Casync addresses this problem by fragmenting the images into "chunks" and by downloading only those chunks that have changed, to successfully update the image.

## How to use

Casync must be used in a two-step fashion (three if you count building the container):

**(0)** The first time you use casync, we must build the singularity container, you can do it by:

`
sudo singularity build --force Casync casync.def 
`

**(1)** First, we must "chunk" the image in the local server into small fragments or chunks. We can do this by:

`
singularity run Casync -chunk MYIMAGE.squashfs
`
This will create a file called app.caibx, which includes an index of all the chunks, and the chunks inside a folder called default.castr/. 
Now, upload both the app.caibx and the folder default.castr/ in your server so it can be accessed through internet.

**(2)** Second, we ssh to our remote repo and we update our image by doing:

`
singularity run Casync -sync http://myserver.com/myapp/app.caibx -seed myREPOIMG.squashfs  -new MYUPDATEDIMG.squashfs
`

