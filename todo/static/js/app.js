function speak(t_id) {
    var text = document.getElementById(t_id).innerHTML;
    responsiveVoice.speak(text)
}
