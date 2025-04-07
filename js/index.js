$(window).on('load', function () {
    const $loader = $(`
      <div class="loader">
        <div class="loader-text">🐮 Moo</div>
      </div>
    `);
    $('body').prepend($loader);
    setTimeout(() => {
      $loader.addClass('fade-out');
  
      setTimeout(() => {
        $loader.remove();
        $('body').addClass('visible');
      }, 500);
    }, 1500);
  });
  
  function interact() {
    alert("Redirecting to Discord invite...");
    window.location.href = "https://discord.com/oauth2/authorize?client_id=1345476025005510747&permissions=8590395469&scope=bot";
}
