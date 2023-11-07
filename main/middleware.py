# # middleware.py

# from django.http import HttpResponseForbidden

# class WiFiRestrictionMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         restricted_view_url_prefix = '/room/'
#         if request.path.startswith(restricted_view_url_prefix):
#             allowed_ip_addresses = ["192.168.7.9","192.168.7.10","192.168.7.11"]
#             user_ip = request.META.get('REMOTE_ADDR')

#             if user_ip not in allowed_ip_addresses:
#                 return HttpResponseForbidden("Access denied. Not on the allowed list.")

#         response = self.get_response(request)
#         return response

from django.http import HttpResponseForbidden

class WiFiRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        restricted_view_url_prefix = '/room/'
        if request.path.startswith(restricted_view_url_prefix):
            allowed_ip_addresses = ["192.168.7.9", "192.168.7.10", "192.168.7.11","127.0.0.1"]
            
            # Use request.META.get('HTTP_X_FORWARDED_FOR') to get the user's IP address
            user_ip = request.META.get('REMOTE_ADDR')
            print("User IP:", user_ip)
            print("Allowed IP Addresses:", allowed_ip_addresses)
            if user_ip:
                user_ip = user_ip.split(',')[0].strip()

            if user_ip not in allowed_ip_addresses:
                return HttpResponseForbidden("Access denied. Not on the allowed list.")

        response = self.get_response(request)
        return response
