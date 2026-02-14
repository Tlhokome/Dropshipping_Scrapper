#I cant access the websites product containers
from bs4 import BeautifulSoup
import requests



headers = {'User-Agent': 'Mozilla/5.0...'} 
html_text = requests.get('https://stevemadden.co.za/collections/sm-sale?gad_source=1&gad_campaignid=23524041505&gbraid=0AAAAABKaaTDImtQJZupm0XSKTbJ8_E77N&gclid=Cj0KCQiA18DMBhDeARIsABtYwT123PNxIcZUwcr0-ZQJ8skmhzR1TRmHz0zhKqaoUhp-SyhzGEqCY7MaAtQnEALw_wcB', headers=headers).text
soup = BeautifulSoup(html_text, 'lxml')    


#Default value for all variables 
shoe_name = None
shoe_salePrice = None
shoe_originalPrice = None
percentOff = None
shoeLink = None
shoeImage = None

#The product container of the first shoe on the page
shoes = soup.find('div', class_='product-container fs-results-product-card svelte-1cj2oxp product-container-visibility-hidden product-card-border fs-product-has-compare more-colors') 
if shoes:
    print('Found the product container')
else:
    None


#<div class="product-container fs-results-product-card svelte-1cj2oxp product-container-visibility-hidden product-card-border fs-product-has-compare more-colors" data-product-id="7214959296649" data-product-position="1" role="group" aria-label="product"><a href="/collections/sm-sale/products/scenic-silver" class="fs-product-image-link svelte-1cj2oxp" aria-label="SCENIC SILVER"><div class="img-container image-wrapper svelte-1cj2oxp"><div class="my-badge-labels badge-align-right"><span class="badge-base my-badge-label sale" style="right: 0px; left: auto;">SALE</span></div>   <div class="fs-badges-wrapper svelte-yjw7vf">  <div class="fs-empty-sale-badge"></div></div> <div class="fs-heart-button-wrapper svelte-11tm4yo fs-heart-button-wrapper-product fs-not-in-wishlist" style="--heart-icon-align: flex-start; --heart-icon-justify-content: flex-start;"><span class="fs-heart-icon-wrapper svelte-11tm4yo"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" width="30px" height="30px" color="var(--product-wish-list-not-checked-color)"><path fill="currentColor" d="M310.3 108.6L257.3 167.2L201.1 109C167.2 73.77 113.2 71.03 81.21 98.88L80.94 99.12C39.31 134.8 37.21 198.7 74.21 237.1L74.24 237.1L256.4 424.1L263.2 417.9C268.1 434.7 275.5 450.4 284.9 464.6L279.4 470.3C266.4 483.2 245.5 483.2 233.5 470.3L39.71 270.5C-16.22 212.5-13.23 116.6 49.7 62.68C98.77 19.96 171.8 23.55 222.2 62.93C227.2 66.83 231.1 71.08 236.5 75.67L256.4 96.64L275.4 75.67C280.1 70.91 285 66.51 290.2 62.5C340.4 23.53 412.5 20.11 463.2 62.68C506.1 100.1 520.7 157.6 507 208.7C492.7 201.1 477.3 197.1 461.2 194.4C469.4 160.9 459.7 123.5 432 99.16C397.6 70.61 344.6 74.22 310.3 108.6zM288 368C288 288.5 352.5 223.1 432 223.1C511.5 223.1 576 288.5 576 368C576 447.5 511.5 512 432 512C352.5 512 288 447.5 288 368zM448 303.1C448 295.2 440.8 287.1 432 287.1C423.2 287.1 416 295.2 416 303.1V351.1H368C359.2 351.1 352 359.2 352 367.1C352 376.8 359.2 383.1 368 383.1H416V431.1C416 440.8 423.2 447.1 432 447.1C440.8 447.1 448 440.8 448 431.1V383.1H496C504.8 383.1 512 376.8 512 367.1C512 359.2 504.8 351.1 496 351.1H448V303.1z"></path></svg></span></div>   <div class="fs-product-main-image-wrapper"><span> <span class="image-wrapper svelte-159yttz"><img src="https://cdn.shopify.com/s/files/1/0035/9405/9887/files/SM11002562-02003-751_02_1000x1000_f2d1b377-3683-427e-90a5-035b65e56f3a.webp?width=560&amp;v=1687254599" decoding="async" alt="SCENIC SILVER" class="product-image svelte-159yttz" loading="eager" fetchpriority="high" width="100"></span></span></div></div></a> <div class="product-content product-card-items-wrapper svelte-1cj2oxp" style="--grid-areas: &quot;title title title title&quot; &quot;compare compare price price&quot; &quot;reviews reviews reviews reviews&quot; "><div class="product-info info-container svelte-1cj2oxp"><div itemscope="" itemtype="//schema.org/Product" class="scheme svelte-zslcl"><meta itemprop="name" content="SCENIC SILVER">  <meta itemprop="description" content=""> <meta itemprop="sku" content="SCENIC-SI-US6-UK3 SCENIC-SI-US7-UK4 SCENIC-SI-US8-UK5 SCENIC-SI-US9-UK6 SCENIC-SI-US10-UK7 SCENIC-SI-US11-UK8 197369041857 197369041871 197369041895 197369041918 197369041932 197369041956"> <meta itemprop="image" content="https://cdn.shopify.com/s/files/1/0035/9405/9887/files/SM11002562-02003-751_02_1000x1000_f2d1b377-3683-427e-90a5-035b65e56f3a.webp?v=1687254599"> <div itemprop="offers" itemscope="" itemtype="//schema.org/Offer"><meta itemprop="priceCurrency" content="ZAR"> <meta itemprop="price" content="595"> <meta itemprop="url" content="/products/scenic-silver"> <meta itemprop="availability" content="https://schema.org/InStock"></div></div> <a class="title-container fs-serp-product-title svelte-f24ry9" href="/collections/sm-sale/products/scenic-silver"><div class="title-wrapper fs-product-title-wrapper svelte-f24ry9"><h2 class="fs_heading_title_cstm"><span class="product-title fs-product-title svelte-f24ry9">SCENIC SILVER</span></h2></div></a> <div class="price-container fs-serp-price svelte-1l6aelb price-is-compare"><div class="fs-price price svelte-1l6aelb" tabindex="0" data-a11y-enhanced="true"><span class="sr-only visually-hidden">Current price: R595.00</span><span class="fs-price-visual" aria-hidden="true"></span>R595.00</div></div> <div class="compare-container svelte-1kxkm4i"><div class="compare fs-compare svelte-1kxkm4i" tabindex="0" data-a11y-enhanced="true"><span class="sr-only visually-hidden">Original price discounted: R1499.00</span><span class="fs-price-visual" aria-hidden="true"></span>R1499.00</div></div> <div class="description-container svelte-1an5uon"><div class="description-wrapper svelte-1an5uon"><span class="description fs-description svelte-1an5uon"></span></div></div> <div class="vendor-container fs-product-vendor-container svelte-1yv46dz"><div class="vendor fs-product-vendor svelte-1yv46dz">undefined</div></div> <div class="sku-container fs-sku-container svelte-173goz1"><small class="sku fs-sku svelte-173goz1"><small class="fs-sku-prefix" data-svelte-h="svelte-1c1ki8f">SKU: #</small>SCENIC-SI-US6-UK3 SCENIC-SI-US7-UK4 SCENIC-SI-US8-UK5 SCENIC-SI-US9-UK6 SCENIC-SI-US10-UK7 SCENIC-SI-US11-UK8 197369041857 197369041871 197369041895 197369041918 197369041932 197369041956</small></div> <div title="Be the first to review this product" class="reviews-container fs-serp-reviews} svelte-1c0luew"></div> <div class="add_wish_class"><div class="desktop_wishlist"><span class="wishlist_btn_phone" role="button" tabindex="0"><svg viewBox="0 0 24 24"><path d="M22 3.1c2.7 2.2 2.6 7.2.1 9.7-2.2 2.8-7.4 8.1-9.3 9.6-.5.4-1.1.4-1.6 0-1.8-1.5-7-6.8-9.2-9.6-2.6-2.6-2.7-7.6 0-9.7C4.6.5 9.7.7 12 4.2 14.3.8 19.3.5 22 3.1zm-.7.8c-2.4-2.4-7.2-2-8.9 1.5-.1.3-.4.4-.7.2-.1 0-.2-.1-.2-.2-1.6-3.5-6.5-4-8.9-1.5C.4 5.6.5 10 2.7 12.2c2.2 2.7 7.3 8 9.1 9.4.1.1.2.1.3 0 1.8-1.4 6.9-6.7 9.1-9.5 2.3-2.1 2.4-6.5.1-8.2z"></path></svg></span></div><div class="fast_product_quick_shop"><div class="details_right_wrap"><button type="button" class="quick_add_btnn" data-handle="/products/scenic-silver" data-source="Collection Page">ADD+</button></div></div><p class="color-count"><span class="pro_number" data-tags="[&quot;#scenic-pink&quot;,&quot;#scenic-silver&quot;]" data-ct="2 COLORS"></span></p></div><div class="my-colorswatch-labels">2 <span>COLOURS </span></div></div></div> <div class="actions svelte-1cj2oxp"> </div><amazon-delivery-message style="width: 100%;" product-external-id="gid://shopify/Product/7214959296649" message-text="options-available"></amazon-delivery-message></div>

#shoe_name = shoes.find('h3', class_ = 'chakra-text css-15jo16m').text.strip()
#shoe_salePrice = shoes.find('h3', class_ = 'chakra-text css-0').text.strip() 

#originalPrice = shoes.find('span', class_ = 'css-idkz9h').text.strip()  
#num = 'R ' + originalPrice.split()[-1]  
#shoe_originalPrice = num

#percent = shoes.find('span', class_ = 'chakra-badge css-xq3ptc').text.strip()
#percentOff = percent + ' off'


#anchor = shoes.find('a', class_ = 'chakra-link product-tile  css-117gxsg')
#if anchor:
#    href = anchor.get('href')
#    if href:
#        shoeLink = 'https://za.puma.com' + href
#    else:
#        print('No href attribute found on anchor')
#else:
#    print('No anchor tag found inside css-19w3d8n')



#image = shoes.find('img', class_ = 'chakra-image css-169s1qj')
#if image:
#    shoeImage = image.get('src')
#else:    
#    print('No image tag found inside css-19w3d8n')



#print(f''' 
#    Shoe name: {shoe_name}
#    Sale price: {shoe_salePrice}
#    Original price: {shoe_originalPrice}
#    Discount percentage: {percentOff}
#    More info: {shoeLink}
#    Shoe picture: {shoeImage}''')




