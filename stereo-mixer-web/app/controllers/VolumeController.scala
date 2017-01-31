package controllers

import javax.inject.{Inject, Singleton}
import play.api.mvc.{Action, Controller}

@Singleton
class VolumeController @Inject() extends Controller {
	def get = Action {
		Ok(views.html.volume(volume(channel = 1)))
	}

	def getVolume(channel: Int) = Action {
		// 現在のボリュームを返す
		Ok(volume(channel).toString);
	}

	def put (channel: Int, vol: Int) = Action {
		Ok(views.html.volume(volume(channel = 1)))
	}


	private def volume(channel: Int): Int = {
		// ここで現在のボリュームを取得

		return channel * 100;
	}

	private def setVolume(channel: Int, vol: Int) {
		// ここでボリューム設定を実行
		// SPI 通信でボリュームを制御するしくみを叩く

	}
}


