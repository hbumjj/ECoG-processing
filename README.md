# ECoG-processing


The ECoG data is an electrode inserted into the lerft audio area and a signal measured by earlobe 

this processing use Synchronizing averaging and add triger (several stimulations) 

ref: 

![333](https://user-images.githubusercontent.com/95017140/152637019-1d0f9c2f-f751-4ffd-a6d1-7a89c332101a.jpg)


Data info

- sampling rate: 1000Hz
- Each trial (Measuring by stimulation) consist of 2 sec (-0.3 pre-stimulation and +1.699 post-stimulation)
- remove noise using Synchronizing averaging (ensemble averaging)
- 8 stimulations ('Ears: 1', 'Eyes: 2', 'Throat: 3', 'Nose: 4', 'Sam: 5', 'Oh: 6', 'Gu: 7', 'Ship: 9')
- Stimulating words and information on the stimulation time point is recored in the third column of the ECoG File 


Auditory evoked potential (AEP) according to the stimulus word is obtained and compared 

