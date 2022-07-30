import requests
from uuid import uuid4
from os import urandom
from hashlib import md5

class HideOnline:
	def __init__(
			self,
			title_id: str = "4A02",
			sdk: str = "UnitySDK-2.63.190312"):
		self.api = "https://4a02.playfabapi.com/Client"
		self.headers = {
			"user-agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G9880 Build/RP1A.2007201.012)",
			"x-playfabsdk": "UnitySDK-2.63.190312",
			"x-unity-version": "2018.4.36f1",
			"content-type": "application/json"
		}
		self.sdk = sdk
		self.user_id = None
		self.title_id = title_id
		self.session_ticket = None

	def generate_device_id(self):
		return md5(urandom(15)).hexdigest()

	def register(
			self,
			get_character_inventories: bool = False,
			get_character_list: bool = False,
			get_player_profile: bool = True,
			get_player_statistics: bool = False,
			get_title_data: bool = False,
			get_user_account_info: bool = False,
			get_user_data: bool = False,
			get_user_inventory: bool = False,
			get_user_read_only_data: bool = False,
			get_user_virtual_currency: bool = False,
			show_avatar_url: bool = False,
			show_banned_until: bool = False,
			show_campaign_attributions: bool = False,
			show_contact_emails: bool = False,
			show_created: bool = False,
			show_display_name: bool = False,
			show_last_login: bool = False,
			show_linked_accounts: bool = False,
			show_locations: bool = False,
			show_memberships: bool = False,
			show_origination: bool = False,
			show_notification_registrations: bool = False,
			show_statistics: bool = False,
			show_tags: bool = True,
			show_total_value_to_date_usd: bool = False,
			show_values_to_date: bool = False):
		data = {
			"AndroidDeviceId": self.generate_device_id(),
			"CreateAccount": True,
			"InfoRequestParameters": {
				"GetCharacterInventories": get_character_inventories,
				"GetCharacterList": get_character_list,
				"GetPlayerProfile": get_player_profile,
				"GetPlayerStatistics": get_player_statistics,
				"GetTitleData": get_title_data,
				"GetUserAccountInfo": get_user_account_info,
				"GetUserData": get_user_data,
				"GetUserInventory": get_user_inventory,
				"GetUserReadOnlyData": get_user_read_only_data,
				"GetUserVirtualCurrency": get_user_virtual_currency,
				"ProfileConstraints": {
					"ShowAvatarUrl": show_avatar_url,
					"ShowBannedUntil": show_banned_until,
					"ShowCampaignAttributions": show_campaign_attributions,
					"ShowContactEmailAddresses": show_contact_emails,
					"ShowCreated": show_created,
					"ShowDisplayName": show_display_name,
					"ShowLastLogin": show_last_login,
					"ShowLinkedAccounts": show_linked_accounts,
					"ShowLocations": show_locations,
					"ShowMemberships": show_memberships,
					"ShowOrigination": show_origination,
					"ShowPushNotificationRegistrations": show_notification_registrations,
					"ShowStatistics": show_statistics,
					"ShowTags": show_tags,
					"ShowTotalValueToDateInUsd": show_total_value_to_date_usd,
					"ShowValuesToDate": show_values_to_date
				}
			},
			"TitleId": self.title_id
		}
		return requests.post(
			f"{self.api}/LoginWithAndroidDeviceID?sdk={self.sdk}",
			json=data,
			headers=self.headers).json()

	def login_with_session_ticket(self, session_ticket: str):
		self.session_ticket = session_ticket
		self.headers["x-authorization"] = self.session_ticket

	def get_photon_token(self):
		data = {"PhotonApplicationId": uuid4()}
		return requests.post(
			f"{self.api}/GetPhotonAuthenticationToken?sdk={self.sdk}",
			json=data,
			headers=self.headers).json()

	def get_title_data(
			self,
			keys: list = ["actualVersionAndroid", "gameConfigAndroid.v491"]):
		data = {"Keys": keys}
		return requests.post(
			f"{self.api}/GetTitleData?sdk={self.sdk}",
			json=data,
			headers=self.headers).json()

	def get_server_time(self):
		return requests.post(
			f"{self.api}/GetTime?sdk={self.sdk}",
			headers=self.headers).json()

	def get_store_items(
			self,
			catalog_version: str = "Virtual",
			store_id: str = "General"):
		data = {
			"CatalogVersion": catalog_version,
			"StoreId": store_id
		}
		return requests.post(
			f"{self.api}/GetStoreItems?sdk={self.sdk}",
			json=data,
			headers=self.headers).json()

	def get_account_info(self):
		data = {
			"FunctionName": "getPlayer",
			"RevisionSelection": "Live",
			"SpecificRevision": 0,
		}
		return requests.post(
			f"{self.api}/ExecuteCloudScript?sdk={self.sdk}",
			json=data,
			headers=self.headers).json()

	def get_video_ad_reward(self):
		data = {
			"FunctionName": "giveVideoAdReward",
			"RevisionSelection": "Live",
			"SpecificRevision": 0,
		}
		return requests.post(
			f"{self.api}/ExecuteCloudScript?sdk={self.sdk}",
			json=data,
			headers=self.headers).json()

	def activate_gift_offer(self, gift_name: str):
		data = {
			"FunctionName": "activateGiftOffer",
			"FunctionParameter": {
				"giftName": gift_name
			},
			"RevisionSelection": "Live",
			"SpecificRevision": 0,
		}
		return requests.post(
			f"{self.api}/ExecuteCloudScript?sdk={self.sdk}",
			json=data,
			headers=self.headers).json()

	def check_if_has_gift(self, gift_name: str):
		data = {
			"FunctionName": "checkIfHasGift",
			"FunctionParameter": {
				"giftName": gift_name
			},
			"RevisionSelection": "Live",
			"SpecificRevision": 0,
		}
		return requests.post(
			f"{self.api}/ExecuteCloudScript?sdk={self.sdk}",
			json=data,
			headers=self.headers).json()

	def open_gift_loot_box(self, gift_name: str):
		data = {
			"FunctionName": "openGiftLootBox",
			"FunctionParameter": {
				"giftName": gift_name
			},
			"RevisionSelection": "Live",
			"SpecificRevision": 0,
		}
		return requests.post(
			f"{self.api}/ExecuteCloudScript?sdk={self.sdk}",
			json=data,
			headers=self.headers).json()

	def set_nickname(self, nickname: str):
		data = {
			"FunctionName": "setNickname",
			"FunctionParameter": {
				"nickname": nickname
			},
			"RevisionSelection": "Live",
			"SpecificRevision": 0,
		}
		return requests.post(
			f"{self.api}/ExecuteCloudScript?sdk={self.sdk}",
			json=data,
			headers=self.headers).json()

	def equip_items(
			self,
			skin: str = "s_male1a",
			weapon: str = "w_rifle3b",
			pose: str = "p_1",
			avatar: str = "a_96",
			emoji: str = "e_0"):
		data = {
			"FunctionName": "equipItems",
			"FunctionParameter": {
				"equipment": {
					"skin": skin,
					"weapon": weapon,
					"pose": pose,
					"avatar": avatar,
					"emoji": emoji
				}
			},
			"RevisionSelection": "Live",
			"SpecificRevision": 0,
		}
		return requests.post(
			f"{self.api}/ExecuteCloudScript?sdk={self.sdk}",
			json=data,
			headers=self.headers).json()
