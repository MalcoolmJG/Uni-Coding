using UnityEngine;
using System.Collections;
using 
UnityEngine.SceneManagement;
#if UNITY_EDITOR
using UnityEditor;
#endif

public class MainMenu : MonoBehaviour {
	public void LoadLevel (string levelName) {
		SceneManager.LoadScene(levelName);
	}
	public void QuitGame() {
		#if UNITY_EDITOR
		if (EditorApplication.isPlaying)// Allows you to exit the game through the editor
			EditorApplication.isPlaying = false;
		#else
		Application.Quit();
		#endif
	}
}