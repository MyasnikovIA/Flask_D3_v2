<?php
trait CheckBoxTrait
{
    public $caption;
    public $activ;
	function __construct($attrs,$parent)
	{
            $this->CmpType = 'CheckBox';
            BaseCtrl::getProperties($attrs, $this);
            $this->readonly = getBooleanAttr('readonly', $attrs, false);
            $this->checked = getBooleanAttr('checked', $attrs, false);
            RemoveArrKeyRtrn($attrs, 'checked');
            $vcheck = ArrKeyRtrn($attrs, 'valuechecked', '1');
            $vuncheck = ArrKeyRtrn($attrs, 'valueunchecked', '0');
            if($this->value == $vcheck)
                $this->checked = true;
            if($this->value == $vuncheck)
                $this->checked = false;

            BaseCtrl::__construct($attrs,$parent);
            
            $this->attrs['valuechecked'] = $vcheck;
            $this->attrs['valueunchecked'] = $vuncheck;
            //$this->SetSysInfo(include_css('Components/CheckBox/css/CheckBox'));
            //$this->SetSysInfo(include_js('Components/CheckBox/js/CheckBox.js'));
	}

	function SetInnerText($text)
	{
		//здесь ничего не должно быть
		null;
	}

    function GetText(&$text)
    {
        $text = '<div '.$this->GetAttrString().' '.$this->GetContAttrString().' class="'.implode(' ',$this->class).'" '.implode(' ',$this->events).$this->ctrlstyle.'><label><input type="checkbox" '.$this->disabled.(($this->checked)?'checked="checked"':'').(($this->readonly)?' readonly="readonly"':'').$this->disabled.' /><span>'.$this->caption.'</span></label></div>';
    }

	function Show()
	{
            $onchange = '';
                if (isset($this->events['onchange']))
                {
                    $onchange = $this->events['onchange'];
                    unset($this->events['onchange']);
                }
		$this->GetText($this->text);
		
		if($this->parent)
			$this->parent->SetInnerText($this->text);
		else
			print $this->text;
			
		BaseCtrl::Show();
	}
}
?>
