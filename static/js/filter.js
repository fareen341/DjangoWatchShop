$(document).ready(function(){
    $('input[type="checkbox"]').click(function() {
        if ($('input[type="checkbox"]:checked').length > 0) {
            $('.products >div').hide();
            $('input[type="checkbox"]:checked').each(function() {
                $('.products >div[data-category=' + this.id + ']').show();
            });
        } else {
            $('.products >div').show();

        }
    });
    
});