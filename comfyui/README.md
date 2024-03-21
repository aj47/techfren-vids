# If you just want the results without installing:
use this link:
https://replicate.com/fofr/face-to-many (you have to set up billing)

# To run locally:
1. [Download pinokio](https://pinokio.computer/)
2. install pinokio
3. run pinokio and click the discover button 
![image](https://github.com/aj47/techfren-vids/assets/8023513/60057147-820c-438e-bbf4-197528fdf0ee)
4. search for comfyui and download it
<img src="https://github.com/aj47/techfren-vids/assets/8023513/d4d55f24-d035-4efe-b5f2-155e8b7d8dbe" width="400" height="400"/>

5. after downloaded, click install (you might need to install a few times for some reason) ![image](https://github.com/aj47/techfren-vids/assets/8023513/88a42758-f0b7-4b83-b414-4201fd726b2e)
6. click start to run the project (might need to click run as well) ![image](https://github.com/aj47/techfren-vids/assets/8023513/b26814e7-4641-4547-b9e6-41da22392ed7)
7. click the URL shown to open the UI ![image](https://github.com/aj47/techfren-vids/assets/8023513/c4c7428d-ee63-44e6-b1d6-15e6228754b7)
8. download the .json file in this repository https://github.com/aj47/techfren-vids/blob/main/comfyui/face-to-many.json
9. click the load button in the UI and load the downloaded .json file ![image](https://github.com/aj47/techfren-vids/assets/8023513/c3141b0d-7ec2-4eed-9a68-7dda1865c1cd)
10. click the manager button in the UI ![image](https://github.com/aj47/techfren-vids/assets/8023513/c8943b32-2600-4731-b708-67f3f2cae141)
11. click install missing custom nodes ![image](https://github.com/aj47/techfren-vids/assets/8023513/33e77b9e-4c72-430c-8d3b-971ea1fe02ca)
12. after thats done click 'install models' and then search 'instantid' and install 'ip-adapter.bin' ![image](https://github.com/aj47/techfren-vids/assets/8023513/bf92a339-42e8-4ca0-bd38-4d34d5736c4b)
13. download instantid controlnet model from here: https://huggingface.co/InstantX/InstantID/resolve/main/ControlNetModel/diffusion_pytorch_model.safetensors?download=true
14. place the file from 13 in your controlnet folder like this: C:\Users\<YOUR USERNAME>\pinokio\api\comfyui.git\app\models\controlnet (you can find the files folder from pinokio by clicking the files button) ![image](https://github.com/aj47/techfren-vids/assets/8023513/abe1b654-42f5-4a60-9401-bbbd9163af4d)
15. download aldebobaseXL from here: https://huggingface.co/frankjoshua/albedobaseXL_v13/resolve/main/albedobaseXL_v13.safetensors?download=true
16. place the file from 15 in your checkpoints folder like: C:\Users\<YOUR USERNAME>\pinokio\api\comfyui.git\app\models\checkpoints
17. download ps1 LORA from: https://huggingface.co/artificialguybr/ps1redmond-ps1-game-graphics-lora-for-sdxl/resolve/main/PS1Redmond-PS1Game-Playstation1Graphics.safetensors?download=true
18. place the file from step 16 in your lora folder like: C:\Users\<YOUR USERNAME>\pinokio\api\comfyui.git\app\models\loras
19. download and extract antelopev2 from here: https://huggingface.co/MonsterMMORPG/tools/resolve/main/antelopev2.zip
20. place extracted antelopev2 folder in: C:\Users\<YOUR USERNAME>\pinokio\api\comfyui.git\app\models\insightface\models




