import numpy as np
import pyproj
import h5py
import matplotlib.pyplot as plt

def orthometric(coords):
    
    wgs84 = pyproj.crs.CRS.from_epsg(4979)
    wgs84_egm08 = pyproj.crs.CRS.from_epsg(3855)
    tform = pyproj.transformer.Transformer.from_crs(crs_from=wgs84, crs_to=wgs84_egm08)
    _, _, z_g = tform.transform(coords[:,0], coords[:,1], coords[:,2])
    
    return z_g

def file2pointcloud(filename):
    
    file = h5py.File(filename, 'r')

    data = {}
    for beam in ['gt1l', 'gt1r', 'gt2l', 'gt2r', 'gt3l', 'gt3r']:
        if beam in list(file.keys()):
            distance = file[beam]['heights']['dist_ph_along'][()]
            height   = file[beam]['heights']['h_ph'][()]
            lat      = file[beam]['heights']['lat_ph'][()]
            lon      = file[beam]['heights']['lon_ph'][()]

            height = orthometric(np.array([lat, lon, height]).T)
            
            data[beam] = {'distance':distance,
                            'height':height}
            
    return data

def pointcloud2waveform(pointclouds):
    
    waveforms = {}
    for beam, data in pointclouds.items():
        distance = data['distance']
        height = data['height']
        
        assert distance.shape == height.shape

        x = [0,20]
        y = np.arange(-10, 10.1, 0.1)

        H, _,_  = np.histogram2d(distance, height, bins=[x,y])

        waveforms[beam] = {"intensity": H.reshape(-1),
                           "elevation": y[:-1]}
        
    return waveforms

def displayWaveforms(waveforms):
    show_waves = input("Display Waveforms? [yes|no]")

    if show_waves == "yes":
        for beam, data in waveforms.items():
            plt.figure()
            plt.barh(data['elevation'], data['intensity'], height=0.1)
            plt.title(beam, fontsize=16)
            plt.xlabel("# photons", fontsize=14)
            plt.ylabel("Elevation", fontsize=14)

    elif show_waves == "no":
        print("OK")

    else:
        print("I don't understand...")
        displayWaveforms(waveforms)
