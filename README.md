# Instagram_Message_To_Json

## Basic Start

You will need access to the following:
* An Instagram Business Account
* A Facebook Page connected to that account
* A Facebook Developer account that can perform Tasks with atleast "Moderate" level access on that Page
* A registered Facebook App with Basic settings configured


## Developer Requirements
* Access token and webhooks concepts are similar. Instagram Messaging will require instagram_manage_messages in the Page Access Token and Instagram topic webhooks subscribed.
## Facebook Login
* Add the Facebook Login product to your app in the App Dashboard.
![alt text](https://scontent.fagr1-2.fna.fbcdn.net/v/t39.2365-6/142024493_1510314282501283_2452978316199914465_n.png?_nc_cat=108&ccb=1-5&_nc_sid=ad8a9d&_nc_ohc=foFoaV0h4GsAX_Yswe4&_nc_ht=scontent.fagr1-2.fna&oh=91592d66ab88e2fedb1632c0227557ca&oe=612B73F4)

You can leave all settings on their defaults. If you are implementing Facebook Login manually, enter your redirect_uri in the Valid OAuth redirect URIs field. If you will be using one of our SDKs, you can leave it blank.

Facebook login is required to get the appropriate access token on assets/pages that are not owned by the developer. For development purpose, you can also leverage Graph API Explorer to generate the appropriate access tokens for assets that you owned and skip to step 3.

## Get the Page Access Token via Instagram Developer Dashboard Tool
* Optionally, if you own the assets(IG account and FB page) that you want to onboard to Instagram Messaging, you can leverage the Instagram setup tool under the Developer App Dashboard to allow you to easily setup Page Access Tokens and Webhooks. You can find the tool under Developer app dashboard → Messenger → Instagram Settings. Existing way of configuring tokens and webhook will still work, but this tool will give you an easier way to setup your environment.
![alt text](https://scontent.fagr1-2.fna.fbcdn.net/v/t39.2365-6/196275801_927883678049780_255440934045349593_n.png?_nc_cat=106&ccb=1-5&_nc_sid=ad8a9d&_nc_ohc=iPrU-Na6OQwAX82_NWT&_nc_ht=scontent.fagr1-2.fna&oh=d61ea323fb169308286fd708c1409dad&oe=612A4987)

## Enable Message Control Connected Tools Settings
* In order to manage Instagram messages via API, IG business accounts will need to enable the connected tools toggle under message control settings.
![alt text](https://scontent.fagr1-1.fna.fbcdn.net/v/t39.2365-6/161856968_298941651650715_9153695413459699473_n.png?_nc_cat=107&ccb=1-5&_nc_sid=ad8a9d&_nc_ohc=CbdeuGLV6ZcAX9Y_RkW&_nc_ht=scontent.fagr1-1.fna&oh=a0a004f6e4f6fb8bc42259f73f0d68fa&oe=612B6657)



## Run this file 
* Download this file and go to the folder bot.py resides, ecdit the file and replace the page access token with token of the page connected with the app and in the terminal run following command
 ```
 python bot.py
 ```

To test locally, create an Ngrok server at port 5000.

Copy the URL obtained from Ngrok.
Paste this * webhoohook url * and * token = "done" * in 4th point of changing your webhook phase

## Changing Your Webhook
To edit your webhook URL or verify token, do the following:

* In your app dashboard, click the "Add Product" button.
* Add the "Webhooks" product. That will present you with an interface to edit your webhook.
* In the Webhooks settings, click the 'Edit Subscriptions' for Instaram option button.
* Update your webhook details.
* Click the 'Verify and Save' button. The Messenger Platform will verify your webhook and save the new details on success.





