(function(a){function t(t){for(var n,o,l=t[0],s=t[1],c=t[2],v=0,d=[];v<l.length;v++)o=l[v],Object.prototype.hasOwnProperty.call(r,o)&&r[o]&&d.push(r[o][0]),r[o]=0;for(n in s)Object.prototype.hasOwnProperty.call(s,n)&&(a[n]=s[n]);u&&u(t);while(d.length)d.shift()();return i.push.apply(i,c||[]),e()}function e(){for(var a,t=0;t<i.length;t++){for(var e=i[t],n=!0,o=1;o<e.length;o++){var s=e[o];0!==r[s]&&(n=!1)}n&&(i.splice(t--,1),a=l(l.s=e[0]))}return a}var n={},r={app:0},i=[];function o(a){return l.p+"../static/js/"+({about:"about"}[a]||a)+"."+{about:"a2e3aa8a"}[a]+".js"}function l(t){if(n[t])return n[t].exports;var e=n[t]={i:t,l:!1,exports:{}};return a[t].call(e.exports,e,e.exports,l),e.l=!0,e.exports}l.e=function(a){var t=[],e=r[a];if(0!==e)if(e)t.push(e[2]);else{var n=new Promise((function(t,n){e=r[a]=[t,n]}));t.push(e[2]=n);var i,s=document.createElement("script");s.charset="utf-8",s.timeout=120,l.nc&&s.setAttribute("nonce",l.nc),s.src=o(a);var c=new Error;i=function(t){s.onerror=s.onload=null,clearTimeout(v);var e=r[a];if(0!==e){if(e){var n=t&&("load"===t.type?"missing":t.type),i=t&&t.target&&t.target.src;c.message="Loading chunk "+a+" failed.\n("+n+": "+i+")",c.name="ChunkLoadError",c.type=n,c.request=i,e[1](c)}r[a]=void 0}};var v=setTimeout((function(){i({type:"timeout",target:s})}),12e4);s.onerror=s.onload=i,document.head.appendChild(s)}return Promise.all(t)},l.m=a,l.c=n,l.d=function(a,t,e){l.o(a,t)||Object.defineProperty(a,t,{enumerable:!0,get:e})},l.r=function(a){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(a,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(a,"__esModule",{value:!0})},l.t=function(a,t){if(1&t&&(a=l(a)),8&t)return a;if(4&t&&"object"===typeof a&&a&&a.__esModule)return a;var e=Object.create(null);if(l.r(e),Object.defineProperty(e,"default",{enumerable:!0,value:a}),2&t&&"string"!=typeof a)for(var n in a)l.d(e,n,function(t){return a[t]}.bind(null,n));return e},l.n=function(a){var t=a&&a.__esModule?function(){return a["default"]}:function(){return a};return l.d(t,"a",t),t},l.o=function(a,t){return Object.prototype.hasOwnProperty.call(a,t)},l.p="/",l.oe=function(a){throw console.error(a),a};var s=window["webpackJsonp"]=window["webpackJsonp"]||[],c=s.push.bind(s);s.push=t,s=s.slice();for(var v=0;v<s.length;v++)t(s[v]);var u=c;i.push([0,"chunk-vendors"]),e()})({0:function(a,t,e){a.exports=e("56d7")},"56d7":function(a,t,e){"use strict";e.r(t);e("e260"),e("e6cf"),e("cca6"),e("a79d");var n=e("2b0e"),r=function(){var a=this,t=a.$createElement,e=a._self._c||t;return e("v-app",[e("my_app_bar"),e("v-content",[e("v-fade-transition",{attrs:{mode:"out-in"}},[e("router-view")],1)],1),e("v-footer",{attrs:{padless:""}},[e("v-col",{staticClass:"text-center",attrs:{cols:"12"}},[a._v(" "+a._s((new Date).getFullYear())+" — "),e("strong",[a._v("The Kanji Team")])])],1)],1)},i=[],o=function(){var a=this,t=a.$createElement,e=a._self._c||t;return e("div",[e("v-navigation-drawer",{staticStyle:{background:"linear-gradient(to bottom, #00416A,#E4E5E6)"},attrs:{dark:"",clipped:"",app:""},model:{value:a.drawer,callback:function(t){a.drawer=t},expression:"drawer"}},[e("v-list",a._l(a.items,(function(t,n){var r=t[0],i=t[1],o=t[2];return e("v-list-item",{key:n,attrs:{to:{path:o},link:""}},[e("v-list-item-icon",[e("v-icon",[a._v(a._s(r))])],1),e("v-list-item-content",[e("v-list-item-title",[a._v(a._s(i))])],1)],1)})),1)],1),e("v-app-bar",{staticClass:"mr-5 align-center",staticStyle:{background:"linear-gradient(to right,#00416A, #E4E5E6)"},attrs:{"clipped-left":"",dark:"",app:""}},[e("v-app-bar-nav-icon",{on:{click:function(t){t.stopPropagation(),a.drawer=!a.drawer}}}),e("v-icon",[a._v("filter_hdr")]),e("v-toolbar-title",[a._v(" Kanji")]),e("v-spacer"),e("v-spacer"),e("v-spacer"),e("v-spacer"),e("v-spacer"),e("v-autocomplete",{attrs:{placeholder:"Search...",items:a.searchs,"single-line":"",color:"white","hide-details":"",filled:"",rounded:""},model:{value:a.value,callback:function(t){a.value=t},expression:"value"}}),e("v-btn",{attrs:{color:"white",icon:""},on:{click:function(t){return a.redirect(a.value)}}},[e("v-icon",[a._v("search")])],1)],1),e("v-overlay",{attrs:{value:a.dialog,opacity:"0.8"}},[e("v-dialog",{attrs:{"hide-overlay":"",transition:"out-in"},model:{value:a.dialog,callback:function(t){a.dialog=t},expression:"dialog"}},[e("v-card",[e("v-toolbar",{attrs:{dense:"",dark:"",color:"white"}},[e("v-spacer"),e("v-btn",{attrs:{icon:"",color:"black"},on:{click:function(t){a.dialog=!1}}},[e("v-icon",[a._v("mdi-close")])],1)],1),e("kanji",{attrs:{char:a.single.name,level:a.single.levels,meaning:a.single.meaning,kun:a.single.kun,on:a.single.on}})],1)],1)],1)],1)},l=[],s=function(){var a=this,t=a.$createElement,e=a._self._c||t;return e("v-card",{staticStyle:{background:"linear-gradient(to right, #9cc3db,#D7DDE8)"},attrs:{hover:""}},[e("v-container",[e("v-card-text",[e("v-layout",[e("v-col",[e("div",{staticClass:"display-1"},[a._v(" "+a._s(a.char)+" ")])]),e("v-col",[e("strong",[a._v("Meaning")]),e("div",[a._v(" "+a._s(a.meaning)),e("br")]),e("strong",[a._v("Kun Reading")]),e("div",[e("div",[a._v(a._s(a.kun)+" ")]),e("br")]),e("strong",[a._v("On Reading")]),e("div",[e("div",[a._v(a._s(a.on)+" ")]),e("br")])])],1)],1),e("v-divider",{staticClass:"mx-4"}),e("v-card-actions",[e("v-layout",[e("v-rating",{attrs:{value:4.5,color:"purple",dense:"","half-increments":"",readonly:"",size:"14"}}),e("v-spacer"),e("v-btn",{attrs:{text:"",color:"purple"},on:{click:function(t){return a.jisho(a.char)}}},[a._v(" Learn More ")])],1)],1)],1)],1)},c=[],v={name:"kanji",props:["char","meaning","kun","on","level"],methods:{jisho:function(a){window.open("https://jisho.org/search/"+a+"#kanji")}}},u=v,d=e("2877"),h=e("6544"),p=e.n(h),m=e("8336"),f=e("b0afa"),g=e("99d9"),_=e("62ad"),b=e("a523"),x=e("ce7e"),y=e("a722"),k=e("1d4d"),V=e("2fa4"),w=Object(d["a"])(u,s,c,!1,null,"a863ff82",null),j=w.exports;p()(w,{VBtn:m["a"],VCard:f["a"],VCardActions:g["a"],VCardText:g["b"],VCol:_["a"],VContainer:b["a"],VDivider:x["a"],VLayout:y["a"],VRating:k["a"],VSpacer:V["a"]});var A={name:"my_app_bar",components:{kanji:j},mounted:function(){var a=this;this.axios.get("http://awesomekanji.cf/data_table/kanjis").then((function(t){return a.searchs=t.data}))},data:function(){return{single:{},dialog:!1,items:[["assessment","Box","/"],["scatter_plot","Scatter","scatter"],["border_all","kanji","kanji"]],searchs:[],drawer:!0,value:null}},methods:{redirect:function(a){var t=this;a&&(this.axios.put("http://awesomekanji.cf/data_table/desc/"+a).then((function(a){return t.single=a.data})),this.dialog=!0)}}},C=A,S=e("40dc"),T=e("5bc1"),O=e("c6a6"),D=e("169a"),E=e("132d"),L=e("8860"),P=e("da13"),W=e("5d23"),z=e("34c3"),J=e("f774"),$=e("a797"),B=e("71d9"),F=e("2a7f"),I=Object(d["a"])(C,o,l,!1,null,"9bd863f0",null),M=I.exports;p()(I,{VAppBar:S["a"],VAppBarNavIcon:T["a"],VAutocomplete:O["a"],VBtn:m["a"],VCard:f["a"],VDialog:D["a"],VIcon:E["a"],VList:L["a"],VListItem:P["a"],VListItemContent:W["a"],VListItemIcon:z["a"],VListItemTitle:W["b"],VNavigationDrawer:J["a"],VOverlay:$["a"],VSpacer:V["a"],VToolbar:B["a"],VToolbarTitle:F["a"]});var G={name:"App",components:{my_app_bar:M}},N=G,R=e("7496"),K=e("a75b"),q=e("0789"),H=e("553a"),Y=Object(d["a"])(N,r,i,!1,null,null,null),Z=Y.exports;p()(Y,{VApp:R["a"],VCol:_["a"],VContent:K["a"],VFadeTransition:q["c"],VFooter:H["a"]});e("d3b7");var Q=e("8c4f"),U=function(){var a=this,t=a.$createElement,e=a._self._c||t;return e("v-container",[e("v-layout",[e("v-card",{attrs:{height:"70"}})],1),e("v-layout",{attrs:{"align-content-space-between":""}},[e("v-flex",{attrs:{8:""}},[e("my_card",{attrs:{line:!0}})],1)],1)],1)},X=[],aa=function(){var a=this,t=a.$createElement,e=a._self._c||t;return e("div",[e("v-card",{attrs:{hover:""}},[e("v-card-title",[e("span",[a._v(a._s(a.title))])]),e("v-container",[e("span",[a._v(a._s(a.yAxis))]),a.scatter?e("div",[e("ve-scatter",{attrs:{data:a.chart_data,settings:a.chart_setting}})],1):a._e(),a.line?e("div",[e("ve-line",{attrs:{data:a.chartData,settings:a.chartSettings}})],1):a._e(),a.bar?e("div",[e("ve-bar",{attrs:{data:a.chartData,settings:a.chartSettings}})],1):a._e(),a.box?e("div",[e("ve-candle",{attrs:{data:a.chart_data,settings:a.chart_setting}})],1):a._e(),e("v-layout",[e("v-flex",{attrs:{xs2:""}}),e("v-flex",{attrs:{xs2:""}}),e("span",[a._v(a._s(a.xAxis))])],1)],1),e("v-card-actions")],1)],1)},ta=[],ea=(e("aabe"),{props:{scatter:Boolean,line:Boolean,bar:Boolean,box:Boolean,chart_data:{},chart_setting:{},title:String,yAxis:String,xAxis:String},data:function(){return{chartSettings:{axisSite:{right:["Wanikani"]},yAxisName:["Jisho level","Wanikani"]},chartData:{columns:["kanji","Jisho level","Wanikani"],rows:[{kanji:"亜","Jisho level":"1",Wanikani:"20"},{kanji:"哀","Jisho level":"3",Wanikani:"35"},{kanji:"挨","Jisho level":"3",Wanikani:"37"},{kanji:"愛","Jisho level":"4",Wanikani:"40"},{kanji:"曖","Jisho level":"4",Wanikani:"48"},{kanji:"悪","Jisho level":"5",Wanikani:"56"}]}}},name:"my_card"}),na=ea,ra=e("0e8f"),ia=Object(d["a"])(na,aa,ta,!1,null,"4e42c7eb",null),oa=ia.exports;p()(ia,{VCard:f["a"],VCardActions:g["a"],VCardTitle:g["c"],VContainer:b["a"],VFlex:ra["a"],VLayout:y["a"]});var la={name:"home_line",components:{my_card:oa}},sa=la,ca=Object(d["a"])(sa,U,X,!1,null,null,null),va=ca.exports;p()(ca,{VCard:f["a"],VContainer:b["a"],VFlex:ra["a"],VLayout:y["a"]});var ua=function(){var a=this,t=a.$createElement,e=a._self._c||t;return e("v-container",{attrs:{fluid:""}},[e("v-container",[e("v-container",[e("v-container",[e("v-card",{attrs:{hover:""}},[e("v-card-title",[e("span",[a._v("Inaccuracy of learning Twitter, Aozora, Wikipedia using each sequence")])]),e("v-container",[e("span",[a._v(a._s(a.yAxis))]),e("v-row",[e("v-flex",{attrs:{xs5:""}},[e("v-card",{attrs:{flat:""}},[e("ve-scatter",{attrs:{data:a.chartData1,settings:a.chartSettings}})],1)],1),e("v-flex",{attrs:{xs1:""}}),e("v-flex",{attrs:{xs5:""}},[e("v-card",{attrs:{flat:""}},[e("ve-scatter",{attrs:{data:a.chartData2,settings:a.chartSettings}})],1)],1)],1),e("v-row",[e("v-flex",{attrs:{xs5:""}},[e("v-card",{attrs:{flat:""}},[e("ve-scatter",{attrs:{data:a.chartData3,settings:a.chartSettings}})],1)],1),e("v-flex",{attrs:{xs1:""}}),e("v-flex",{attrs:{xs5:""}},[e("v-card",{attrs:{flat:""}},[e("ve-scatter",{attrs:{data:a.chartData4,settings:a.chartSettings4}})],1)],1)],1),e("v-layout",[e("v-flex",{attrs:{xs2:""}}),e("v-flex",{attrs:{xs2:""}}),e("span",[a._v(a._s(a.xAxis))])],1)],1),e("v-card-actions")],1)],1)],1)],1)],1)},da=[],ha={name:"home_scatter",data:function(){return{chartSettings:{symbolSizeMax:30,symbolSize:20,yAxisName:"                 Percent of inaccuracy"},chartData1:{columns:["level","Twitter"],rows:[{level:"wanikani",Twitter:.14522003034901365},{level:"JLPT",Twitter:.23180428134556577},{level:"Grade",Twitter:.23840837415285512},{level:"Genki",Twitter:.39556962025316456}]},chartSettings2:{symbolSizeMax:30,yAxisName:"                 Percent of inaccuracy"},chartData2:{columns:["level","Aozora"],rows:[{level:"wanikani",Aozora:.15872534142640363},{level:"JLPT",Aozora:.23574338085539717},{level:"Grade",Aozora:.23525864379522915},{level:"Genki",Aozora:.38276069921639544}]},chartSettings3:{symbolSizeMax:30,yAxisName:"                 Percent of inaccuracy"},chartData3:{columns:["level","Wikipedia"],rows:[{level:"wanikani",Wikipedia:.15977069634125782},{level:"JLPT",Wikipedia:.25132382892057026},{level:"Grade",Wikipedia:.2436738519212746},{level:"Genki",Wikipedia:.3693490054249548}]},chartSettings4:{symbolSizeMax:30,symbolSize:20,yAxisName:"                                    Percent of inaccuracy"},chartData4:{columns:["level","Average"],rows:[{level:"wanikani",Average:.15457202270555837},{level:"JLPT",Average:.23962383037384438},{level:"Grade",Average:.23911362328978628},{level:"Genki",Average:.38255977496483834}]}}}},pa=ha,ma=e("0fd9"),fa=Object(d["a"])(pa,ua,da,!1,null,null,null),ga=fa.exports;p()(fa,{VCard:f["a"],VCardActions:g["a"],VCardTitle:g["c"],VContainer:b["a"],VFlex:ra["a"],VLayout:y["a"],VRow:ma["a"]});var _a=function(){var a=this,t=a.$createElement,e=a._self._c||t;return e("v-container",[e("v-layout",[e("v-card",{attrs:{height:"70"}})],1),e("v-layout",[e("v-flex",{attrs:{10:""}},[e("my_card",{attrs:{bar:!0}})],1)],1)],1)},ba=[],xa={name:"home_hist",components:{my_card:oa}},ya=xa,ka=Object(d["a"])(ya,_a,ba,!1,null,null,null),Va=ka.exports;p()(ka,{VCard:f["a"],VContainer:b["a"],VFlex:ra["a"],VLayout:y["a"]});var wa=function(){var a=this,t=a.$createElement,e=a._self._c||t;return e("v-container",[e("v-layout",[e("v-card",{attrs:{height:"70"}})],1),e("v-layout",{attrs:{"align-content-space-between":""}},[e("v-row",[e("v-flex",{attrs:{8:""}},[e("kanji_table")],1)],1)],1)],1)},ja=[],Aa=function(){var a=this,t=a.$createElement,e=a._self._c||t;return e("div",[e("v-card",{attrs:{hover:""}},[e("v-data-table",{staticClass:"elevation-1",attrs:{headers:a.headers,items:a.kanjis,"sort-by":["levels"],"sort-desc":[!0]},scopedSlots:a._u([{key:"item.levels",fn:function(a){var t=a.item;return[e("v-rating",{attrs:{value:t.levels,color:"purple",dense:"","half-increments":"",readonly:"",size:"14"}})]}},{key:"item.detail",fn:function(t){var n=t.item;return[e("v-btn",{attrs:{icon:"",fab:""}},[e("v-icon",{staticClass:"mr-2",attrs:{small:""},on:{click:function(t){return a.open_detail(n)}}},[a._v(" launch ")])],1)]}}])})],1),e("v-overlay",{attrs:{value:a.dialog,opacity:"0.8"}},[e("v-dialog",{attrs:{"hide-overlay":"",transition:"out-in",loading:a.load},model:{value:a.dialog,callback:function(t){a.dialog=t},expression:"dialog"}},[e("v-card",[e("v-toolbar",{attrs:{dense:"",dark:"",color:"white"}},[e("v-spacer"),e("v-btn",{attrs:{icon:"",color:"black"},on:{click:function(t){a.dialog=!1}}},[e("v-icon",[a._v("mdi-close")])],1)],1),e("kanji",{attrs:{char:a.single.name,level:a.single.levels,meaning:a.single.meaning,kun:a.single.kun,on:a.single.on}})],1)],1)],1)],1)},Ca=[],Sa=(e("b0c0"),{components:{kanji:j},mounted:function(){var a=this;this.axios.get("http://awesomekanji.cf/data_table").then((function(t){return a.kanjis=t.data}))},data:function(){return{single:{},dialog:!1,load:!1,headers:[{text:"Kanji",align:"left",sortable:!1,value:"name"},{text:"Hard level",value:"levels"},{text:"Frequency",value:"frequency"},{text:"Strokes",value:"strokes"},{text:"Detail",value:"detail"}],kanjis:[]}},methods:{open_detail:function(a){var t=this;this.load=!0,this.axios.put("http://awesomekanji.cf/data_table/desc/"+a.name).then((function(a){return t.single=a.data})),this.load=!1,this.dialog=!0}}}),Ta=Sa,Oa=e("8fea"),Da=Object(d["a"])(Ta,Aa,Ca,!1,null,null,null),Ea=Da.exports;p()(Da,{VBtn:m["a"],VCard:f["a"],VDataTable:Oa["a"],VDialog:D["a"],VIcon:E["a"],VOverlay:$["a"],VRating:k["a"],VSpacer:V["a"],VToolbar:B["a"]});var La={name:"kanji_page",components:{kanji_table:Ea}},Pa=La,Wa=Object(d["a"])(Pa,wa,ja,!1,null,"050ab9b5",null),za=Wa.exports;p()(Wa,{VCard:f["a"],VContainer:b["a"],VFlex:ra["a"],VLayout:y["a"],VRow:ma["a"]});var Ja=function(){var a=this,t=a.$createElement,e=a._self._c||t;return e("v-container",[e("v-layout",[e("v-card",{attrs:{height:"70"}})],1),e("v-layout",[e("v-flex",{attrs:{10:""}},[e("my_card",{attrs:{box:!0,chart_data:a.data,chart_setting:a.setting,title:a.title,yAxis:a.y_name,xAxis:a.x_name}})],1)],1),e("v-btn",{attrs:{absolute:"",dark:"",fab:"",bottom:"",right:"",color:"blue"},on:{click:function(t){return a.change()}}},[e("v-icon",[a._v("arrow_forward_ios")])],1)],1)},$a=[],Ba={name:"home_hist",components:{my_card:oa},mounted:function(){var a=this;this.axios.get("http://awesomekanji.cf//data_table/box_"+this.val).then((function(t){return a.data.rows=t.data.data,a.title=t.data.title,a.x_name=t.data.x_name,a.y_name=t.data.y_name}))},data:function(){return{val:1,setting:{legendName:{"日K":"kanji"},showDataZoom:!0,start:0,end:100,upColor:"#90CAF9"},title:"",x_name:"",y_name:"",data:{columns:["strokes","open","close","highest","lowest"],rows:[]}}},methods:{change:function(){var a=this;this.val+=1,this.val>2&&(this.val=1),this.axios.get("http://awesomekanji.cf/data_table/box_"+this.val).then((function(t){return a.data.rows=t.data.data,a.title=t.data.title,a.x_name=t.data.x_name,a.y_name=t.data.y_name}))}}},Fa=Ba,Ia=Object(d["a"])(Fa,Ja,$a,!1,null,null,null),Ma=Ia.exports;p()(Ia,{VBtn:m["a"],VCard:f["a"],VContainer:b["a"],VFlex:ra["a"],VIcon:E["a"],VLayout:y["a"]}),n["a"].use(Q["a"]);var Ga=[{path:"/home",name:"home_line",component:va},{path:"/scatter",name:"home_scatter",component:ga},{path:"/hist",name:"home_hist",component:Va},{path:"/",name:"Home_box",component:Ma},{path:"/kanji",name:"kanji_page",component:za},{path:"/about",name:"about",component:function(){return e.e("about").then(e.bind(null,"f820"))}}],Na=new Q["a"]({routes:Ga}),Ra=Na,Ka=e("f309");n["a"].use(Ka["a"]);var qa=new Ka["a"]({}),Ha=e("2819"),Ya=e.n(Ha),Za=e("313e"),Qa=e.n(Za),Ua=e("bc3a"),Xa=e.n(Ua),at=e("a7fe"),tt=e.n(at);n["a"].use(tt.a,Xa.a),n["a"].use(Ya.a),n["a"].prototype.$echarts=Qa.a,n["a"].config.productionTip=!1,new n["a"]({router:Ra,vuetify:qa,render:function(a){return a(Z)}}).$mount("#app")}});
//# sourceMappingURL=app.8e48f450.js.map